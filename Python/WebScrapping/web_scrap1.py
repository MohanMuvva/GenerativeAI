import requests
from bs4 import BeautifulSoup

def clean_text(text):
    return ' '.join(text.split())

def write_element(file, element, level=0):
    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        file.write('\n' + '#' * level + ' ' + clean_text(element.text) + '\n')
    elif element.name == 'p':
        file.write(clean_text(element.text) + '\n\n')
    elif element.name in ['ul', 'ol']:
        for li in element.find_all('li', recursive=False):
            file.write('  ' * level + '• ' + clean_text(li.text) + '\n')
        file.write('\n')
    elif element.name == 'table':
        for row in element.find_all('tr'):
            file.write('  ' * level + '| ' + ' | '.join(clean_text(cell.text) for cell in row.find_all(['th', 'td'])) + ' |\n')
        file.write('\n')
    elif element.name == 'a':
        # Only write the text of the link, not the URL
        file.write(clean_text(element.text) + ' ')
    else:
        for child in element.children:
            if child.name:
                write_element(file, child, level + 1)

# URL to scrape
url = "https://stjosephhospital.com/visiting-st-joseph/"
# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    with open('scraped_data.txt', 'w', encoding='utf-8') as file:
        # Write page title
        title = soup.title.string if soup.title else "No Title"
        file.write(f"# {title}\n\n")
        
        # Find main content
        main_content = soup.find('main') or soup.find('div', class_='content') or soup.body
        
        if main_content:
            for element in main_content.children:
                if element.name:
                    write_element(file, element)
        else:
            file.write("No main content found on the page.")
        
    print("Data successfully scraped and saved to 'scraped_data.txt'")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
