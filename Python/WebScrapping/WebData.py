import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os
from urllib.parse import urljoin

def clean_text(text):
    return ' '.join(text.split())

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content_dict = {}
        main_content = soup.find('main') or soup.find('div', class_='content') or soup.body
        if main_content:
            for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
                if element.name.startswith('h'):
                    content_dict[clean_text(element.text)] = []
                elif element.name == 'p':
                    if content_dict:
                        content_dict[list(content_dict.keys())[-1]].append(clean_text(element.text))
                    else:
                        content_dict['Content'] = [clean_text(element.text)]
        return content_dict
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def save_to_pdf(content_dict, output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    for header, paragraphs in content_dict.items():
        story.append(Paragraph(header, styles['Heading1']))
        story.append(Spacer(1, 12))
        for paragraph in paragraphs:
            story.append(Paragraph(paragraph, styles['Normal']))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 12))

    doc.build(story)

def get_internal_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        base_url = '/'.join(url.split('/')[:3])  # Get the base URL (e.g., https://stjosephhospital.com)
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('/') or href.startswith(base_url):
                full_url = urljoin(base_url, href)
                if full_url.startswith(base_url):  # Ensure it's an internal link
                    links.append(full_url)
        return list(set(links))  # Remove duplicates
    return []

def create_pdf_name(url):
    # Create a filename from the URL
    filename = url.split('://')[-1].replace('/', '_').replace('?', '_').replace('&', '_')
    return f"{filename}.pdf"

# Main URL to start from
main_url = "https://stjosephhospital.com/visiting-st-joseph/"

# Create a directory to store PDFs
os.makedirs("scraped_pdfs", exist_ok=True)

# Get all internal links
all_links = get_internal_links(main_url)

# Scrape each link and create a PDF
for link in all_links:
    content_dict = scrape_website(link)
    if content_dict:
        pdf_name = create_pdf_name(link)
        pdf_path = os.path.join("scraped_pdfs", pdf_name)
        save_to_pdf(content_dict, pdf_path)
        print(f"Data from {link} successfully scraped and saved to '{pdf_path}'")
    else:
        print(f"Failed to scrape {link}")

print("Scraping and PDF creation completed.")
