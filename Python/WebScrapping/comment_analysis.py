import time
import csv  # Import the csv module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from textblob import TextBlob

# Assuming you have downloaded ChromeDriver and placed it in a known directory
# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\ASUS\\Downloads\\chromedriver-win64\\chromedriver.exe"  # Update this path

chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)
driver.get('https://www.youtube.com/watch?v=GGcuNF24iEs')  # YouTube video URL

# Scroll to load comments
driver.execute_script("window.scrollTo(0, 100);")
time.sleep(5)

for _ in range(10):  # Scroll down multiple times to load more comments
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)

# Extract comments
comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

# Open a CSV file to write the comments and sentiments
with open('comments_sentiment.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Comment', 'Sentiment'])  # Write header

    # Analyze the first 100 comments using TextBlob
    for i, comment in enumerate(comments):
        if i >= 100:  # Limit to the first 100 comments
            break
        text = comment.text
        analysis = TextBlob(text)
        sentiment = 'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'
        writer.writerow([text, sentiment])  # Write comment and sentiment to CSV

# Close WebDriver
driver.quit()
