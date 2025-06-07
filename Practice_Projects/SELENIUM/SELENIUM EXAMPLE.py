from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Set up Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL of NSE stock details page
stock_symbol = "RELIANCE"  # Change to any stock symbol
url = f"https://www.nseindia.com/get-quotes/equity?symbol={stock_symbol}"
print("ffff")
# Open URL
driver.get(url)
time.sleep(5)  # Wait for the page to load

# Extract stock price (Example: Modify selector if required)
try:
    print("eee")
    stock_price_element = driver.find_element(By.ID, "quoteLtp")
    stock_price = stock_price_element.text
    print(f"{stock_symbol} Current Price: ₹{stock_price}")
except Exception as e:
    print("Error fetching stock data:", e)

# Close the driver
driver.quit()
