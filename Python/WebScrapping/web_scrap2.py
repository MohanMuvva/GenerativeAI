import requests
from bs4 import BeautifulSoup

def clean_text(text):
    return ' '.join(text.split())

# URL to scrape
url = "https://stjosephhospital.com/visiting-st-joseph/"
# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Try to find the main content
    content = soup.find('main') or soup.find('div', class_='content') or soup.body

    if content:
        # Open the file to write the scraped data
        with open('scraped_data2.txt', 'w', encoding='utf-8') as file:
            # Write the page title
            title = soup.title.string if soup.title else "No Title"
            file.write(f"Page Title: {title}\n\n")

            # Find all relevant elements
            elements = content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'table', 'a'])
            
            for element in elements:
                if element.name.startswith('h'):
                    # Add newlines before headers for better readability
                    file.write(f"\n\n{element.text.strip().upper()}\n")
                    file.write('=' * len(element.text.strip()) + '\n')  # Underline for headers
                elif element.name == 'p':
                    file.write(f"{clean_text(element.text)}\n\n")
                elif element.name in ['ul', 'ol']:
                    file.write("\n")
                    for li in element.find_all('li'):
                        file.write(f"  • {clean_text(li.text)}\n")
                    file.write("\n")
                elif element.name == 'table':
                    file.write("\nTable Content:\n")
                    for row in element.find_all('tr'):
                        file.write("  | ")
                        file.write(" | ".join(clean_text(cell.text) for cell in row.find_all(['th', 'td'])))
                        file.write(" |\n")
                    file.write("\n")
                elif element.name == 'a' and element.has_attr('href'):
                    file.write(f"Link: {element.text.strip()} - {element['href']}\n")
        
        print("Data successfully scraped and saved to 'scraped_data2.txt'")
    else:
        print("No content found on the page")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
