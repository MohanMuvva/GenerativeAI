import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from textblob import TextBlob

# Set up Selenium WebDriver
chrome_service = Service('path_to_chromedriver')  # Update this with the path to your ChromeDriver
driver = webdriver.Chrome(service=chrome_service)
driver.get('https://www.youtube.com/watch?v=GGcuNF24iEs')  # YouTube video URL

# Scroll to load comments
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(5)

for _ in range(10):  # Scroll down multiple times to load more comments
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)

# Extract comments
comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

# Analyze comments using TextBlob
for comment in comments:
    text = comment.text
    analysis = TextBlob(text)
    sentiment = 'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'
    print(f"Comment: {text}\nSentiment: {sentiment}\n")

# Close WebDriver
driver.quit()
