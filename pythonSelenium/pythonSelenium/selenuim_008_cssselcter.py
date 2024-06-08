import time

from selenium import webdriver

# Chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# some locators - ID, Xpath, CSSSelector, Classname, name, linkText
# need to select which is uniq
# we can use Xpath whether class name or ID available or not
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# creating Xpath
# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit]
# CSS -  tagname[attribute='value'] -> input[type='submit]

# this is a common way to identify the css
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ankit")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
# we can validate text
assert "Success" in message, "Message not found"

time.sleep(3)
driver.close()
