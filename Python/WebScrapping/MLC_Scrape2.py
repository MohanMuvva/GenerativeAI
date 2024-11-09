from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Path to the ChromeDriver
driver_path = 'C:\\Users\\ASUS\\Downloads\\chromedriver-win64\\chromedriver.exe'  # Replace with your actual path to ChromeDriver

# Set up the Chrome driver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# URL of the page with the application status
url = 'https://ceoaperolls.ap.gov.in/AP_MLC_2024/ERO/Status_Update_2024/knowYourApplicationStatus.aspx'
driver.get(url)

# Wait for the page to load completely
driver.implicitly_wait(10)

# Select the "Teachers East/West Godavari" tab by simulating a click
teachers_ew_tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='#teachersEW']"))
)
teachers_ew_tab.click()

# Wait for the search input field to appear
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'txtSearch'))
)

# Clear the search input and enter an empty string (or a wildcard search if needed)
search_input.clear()
search_input.send_keys("")

# Click the "Search" button to trigger the table loading
search_button = driver.find_element(By.ID, 'btnTeachersEW')
search_button.click()

# Wait for the table to load after submission
try:
    table_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, 'table'))
    )
    print("Table found, extracting data...")
except:
    print("Table did not load on the page.")
    driver.quit()
    exit()

# Once the table is loaded, get the page source
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table containing the applicants' data
table = soup.find('table')

if table:
    # Extract the headers from the table
    headers = [header.text.strip() for header in table.find_all('th')]

    # Extract all rows from the table
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the first row as it contains headers
        cols = [col.text.strip() for col in row.find_all('td')]
        rows.append(cols)

    # Convert the extracted data to a DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Save the DataFrame to a CSV file
    df.to_csv('applicant_data.csv', index=False)
    print("Data has been saved to applicant_data.csv.")
else:
    print("No table found on the page.")

# Close the browser
driver.quit()
