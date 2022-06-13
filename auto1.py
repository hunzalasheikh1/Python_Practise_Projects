import os #only for win
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
os.environ["PATH"] += r"chromedriver.exe" #only for win
driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

driver.implicitly_wait(5)


sum1 = driver.find_element_by_id("sum1")
sum2 = driver.find_element_by_id("sum2")

no_button = driver.find_element_by_class_name("at-cm-no-button")
no_button.click()


sum1.send_keys(20)
sum2.send_keys(10)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()







