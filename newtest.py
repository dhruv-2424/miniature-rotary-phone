from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # Path to the Chromium binary
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")  # Disable sandboxing
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
options.add_argument("--window-size=1345x610")

driver = webdriver.Chrome(options=options)
print("script started")
driver.get("https://account.proton.me/mail")
time.sleep(10)

windows_w = driver.execute_script("return window.innerWidth;")
windows_h = driver.execute_script("return window.innerHeight;")

print(f"Windows width: {windows_w}")
print(f"Windows height: {windows_h}")

time.sleep(2)
driver.quit()
