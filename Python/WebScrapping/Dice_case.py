from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")

# Path to ChromeDriver (ensure it's installed and provide the correct path)
chrome_service = Service('C:/Users/ASUS/Downloads/chromedriver-win64/chromedriver.exe')

# Setup Selenium WebDriver with Chrome options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Access the job search URL directly
url = "https://www.dice.com/jobs?q=data%20engineering&countryCode=US&radius=30&radiusUnit=mi&page=2&pageSize=20&language=en"
driver.get(url)

# Allow time for the dynamic content to load
driver.implicitly_wait(10)

# Scroll down the page to load more content dynamically (if necessary)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# Get the page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the driver
driver.quit()

# Prepare lists for scraped data
job_data = []

# Extract job listings (Update tags and classes based on the current site structure)
jobs = soup.find_all('div', class_='card')  # Adjust based on actual structure

# Iterate through jobs and extract required information
for job in jobs:
    try:
        job_name = job.find('h5', class_='job-title').text.strip() if job.find('h5', class_='job-title') else None
        company_name = job.find('span', class_='company-name').text.strip() if job.find('span', class_='company-name') else None
        posted_date = job.find('span', class_='posted-date').text.strip() if job.find('span', class_='posted-date') else None
        employer_type = job.find('span', class_='employer-type').text.strip() if job.find('span', class_='employer-type') else None
        job_description = job.find('p', class_='job-description').text.strip() if job.find('p', class_='job-description') else None
        salary_range = job.find('span', class_='salary-range').text.strip() if job.find('span', class_='salary-range') else None  # Adjust the selector if needed

        # Only append if no None values
        if None not in [job_name, company_name, posted_date, employer_type, job_description, salary_range]:
            job_data.append([job_name, company_name, posted_date, employer_type, job_description, salary_range])
    except AttributeError as e:
        print(f"Error parsing job card: {e}")

# Save the scraped data to a CSV file
csv_file = "scraped_jobs.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job_Name', 'Company_Name', 'Posted_Date', 'Employer_Type', 'Job_Description', 'Salary_Range'])  # Header
    writer.writerows(job_data)

print(f"Data has been written to {csv_file}")
