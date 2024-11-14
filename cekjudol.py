from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import re

# Path to the text file containing URLs (one URL per line)
urls_file = 'urls.txt'

# Read URLs from the file
with open(urls_file, 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

# Configure Chrome options
options = Options()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Path to chromedriver (replace with your actual path or leave blank if in PATH)
chromedriver_path = './chromedriver.exe'

# Initialize the webdriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Function to format URL into a valid filename
def format_filename(url):
    return re.sub(r'[^a-zA-Z0-9]', '_', url)

# Function to take a screenshot of a URL
def take_screenshot(url):
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    filename = format_filename(url) + '.png'
    screenshot_path = filename
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

# Iterate through URLs and take screenshots
for url in urls:
    try:
        take_screenshot(url)
    except Exception as e:
        print(f"Failed to capture screenshot for {url}: {e}")

# Quit the driver
driver.quit()
