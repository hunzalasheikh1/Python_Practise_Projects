import os 
from selenium import webdriver

#only for windows
os.environ['PATH'] += r"chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com")

driver.implicitly_wait(5)

my_element = driver.find_element_by_partial_link_text("TestNG")
my_element.click()
