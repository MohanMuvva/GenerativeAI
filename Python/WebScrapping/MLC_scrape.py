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

# Set up the Chrome driver with options to run in the background
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL of the page with the application status
url = 'https://ceoaperolls.ap.gov.in/AP_MLC_2024/ERO/Status_Update_2024/knowYourApplicationStatus.aspx'
driver.get(url)

# Wait for the page to load completely
driver.implicitly_wait(10)

# Select the "Graduate" option (make sure the correct tab is clicked)
graduate_tab = driver.find_element(By.LINK_TEXT, 'Graduate')
graduate_tab.click()

# Define start and end application IDs
start_app_id = 'F18-0000001'  # Starting application ID
end_app_id = 'F18-9999999'    # Define the last possible application ID

# Function to increment application ID
def increment_app_id(app_id):
    prefix, number = app_id.split('-')
    new_number = int(number) + 1
    return f"{prefix}-{new_number:07d}"

# Function to wait for an element to be clickable
def wait_for_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

# Initialize a list to store all applicant data
all_data = []

# Loop through the application IDs
current_app_id = start_app_id

while current_app_id <= end_app_id:
    try:
        # Locate the search bar and enter the current application ID
        search_input = wait_for_clickable(driver, By.ID, 'txtSearch')
        search_input.clear()
        search_input.send_keys(current_app_id)

        # Scroll the search input element into view to avoid "element not interactable" errors
        driver.execute_script("arguments[0].scrollIntoView();", search_input)

        # Click the "Search" button
        search_button = wait_for_clickable(driver, By.ID, 'btnTeachersEW')
        search_button.click()

        # Wait for the table to load after submission
        try:
            table_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'table'))
            )
            print(f"Table found for {current_app_id}, extracting data...")

            # Get the page source and parse it using BeautifulSoup
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            # Find the table containing the applicants' data
            table = soup.find('table')

            if table:
                # Extract all rows from the table
                rows = []
                for row in table.find_all('tr')[1:]:  # Skip the first row as it contains headers
                    cols = [col.text.strip() for col in row.find_all('td')]
                    rows.append([current_app_id] + cols)  # Add application ID to each row

                # Add the extracted rows to the all_data list
                all_data.extend(rows)

        except Exception as e:
            print(f"Table not found for {current_app_id}: {e}")

        # Increment the application ID for the next iteration
        current_app_id = increment_app_id(current_app_id)

    except Exception as e:
        print(f"Error processing {current_app_id}: {e}")
        current_app_id = increment_app_id(current_app_id)

    # Optional: Pause to avoid overloading the server
    time.sleep(2)

# Create a DataFrame from the collected data and save it to a CSV file
if all_data:
    headers = ["App ID", "PS_NO", "SLNO", "Name", "Relation Name", "House Number", "Age", "AERO Comments", "Ero Comments", "App Status"]
    df = pd.DataFrame(all_data, columns=headers)
    df.to_csv('applicant_data.csv', index=False)
    print("Data has been saved to applicant_data.csv.")
else:
    print("No data was collected.")

# Close the browser
driver.quit()
