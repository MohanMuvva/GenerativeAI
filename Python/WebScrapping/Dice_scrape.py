import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service('C:/Users/ASUS/Downloads/chromedriver-win64/chromedriver.exe')  # Specify the path to your chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_jobs(url, max_jobs=1000):
    driver = setup_driver()
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    job_listings = []
    total_jobs_scraped = 0

    while total_jobs_scraped < max_jobs:  # Loop to handle pagination
        print(f"Scraping page: {driver.current_url}")
        time.sleep(2)  # Wait for the page to load

        # Find job cards
        job_cards = driver.find_elements(By.CSS_SELECTOR, 'dhi-search-card')

        for card in job_cards:
            if total_jobs_scraped >= max_jobs:
                break  # Stop if we've reached the max number of jobs

            try:
                job_title = card.find_element(By.CSS_SELECTOR, 'div.card-header > div > div.d-flex.justify-content-between.title-container > div.overflow-hidden > div > a').text.strip()
            except:
                job_title = 'N/A'

            try:
                company_name = card.find_element(By.CSS_SELECTOR, 'div.card-header > div > div.d-flex.justify-content-between.title-container > div.overflow-hidden > div > span').text.strip()
            except:
                company_name = 'N/A'

            try:
                location = card.find_element(By.CSS_SELECTOR, 'div.card-body.font-small.m-left-20.mobile-m-left-10 > div.d-flex.flex-wrap > div.card-position-type > span').text.strip()
            except:
                location = 'N/A'

            try:
                posted_date = card.find_element(By.CSS_SELECTOR, 'div.card-body.font-small.m-left-20.mobile-m-left-10 > div.d-flex.flex-wrap > div:nth-child(2) > span').text.strip()
            except:
                posted_date = 'N/A'

            try:
                description = card.find_element(By.CSS_SELECTOR, 'div.card-body.font-small.m-left-20.mobile-m-left-10 > div.card-description').text.strip()
            except:
                description = 'N/A'

            job_listings.append({
                'Job Title': job_title,
                'Company': company_name,
                'Location': location,
                'Posted Date': posted_date,
                'Description': description
            })

            total_jobs_scraped += 1  # Increment the count of jobs scraped

        # Check for the "Next" button in the pagination and click it if it exists
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'pagination .pagination-next a.page-link')
            if "disabled" in next_button.get_attribute("class"):
                print("No more pages to scrape.")
                break
            next_button.click()
            time.sleep(5)  # Wait for the next page to load
        except NoSuchElementException:
            print("No more pages to scrape.")
            break
        except ElementClickInterceptedException:
            print("Next button is not clickable, trying again...")
            time.sleep(2)  # Wait a bit and try again
            continue

    driver.quit()
    return job_listings

# URL to scrape
url = "https://www.dice.com/jobs?q=data%20engineering&countryCode=US&radius=30&radiusUnit=mi&pageSize=20&language=en"

# Scrape jobs
all_job_listings = scrape_jobs(url, max_jobs=1000)

# Write to CSV
try:
    with open('job_listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Job Title', 'Company', 'Location', 'Posted Date', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for job in all_job_listings:
            writer.writerow(job)

    print("Job listings successfully scraped and saved to 'job_listings.csv'")
except PermissionError:
    print("Permission denied: Please close the 'job_listings.csv' file if it is open in another program.")