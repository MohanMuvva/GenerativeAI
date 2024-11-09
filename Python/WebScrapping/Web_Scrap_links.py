import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL to scrape
home_url = "https://stjosephhospital.com/"

# Send a GET request to fetch the homepage content
response = requests.get(home_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags with href attributes
    links = soup.find_all('a', href=True)

    # Open a file to save the extracted URLs
    with open('urls.txt', 'w') as file:
        for link in links:
            # Get the absolute URL
            full_url = urljoin(home_url, link['href'])
            file.write(full_url + '\n')  # Save each URL to the text file

    print("URLs successfully scraped and saved to 'urls.txt'")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
