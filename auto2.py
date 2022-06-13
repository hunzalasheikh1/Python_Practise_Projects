#only for windows
import os 
from selenium import webdriver

#only for windows
os.environ['PATH'] += r"chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(5)

download_button = driver.find_element_by_id("downloadButton")
download_button.click()
