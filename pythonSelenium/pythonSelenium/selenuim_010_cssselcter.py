import time
from selenium import webdriver

# Chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()

# url that need to be automated https://rahulshettyacademy.com/angularpractice/
driver.get("https://rahulshettyacademy.com/angularpractice/")



driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# creating Xpath
# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit]
# CSS -  tagname[attribute='value'] -> input[type='submit]  '#ID' also turnout to a css, '.classname' also called as valid css

# if we want to click radio button
# one plugin need to install to validate Xpath and ccs selector
# selectorsHub add in your extensions and restart your browser
# using '#ID' also create css selector
# '.class_name' also a valid css selector
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ankit")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click() # used # ID to create valid selector
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
# we can validate text
assert "Success" in message, "Message not found"
# selenium search from Top left if multiple match there then by indexing
# we can select any match
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(" Hello again")
# to clear above things then, use .clear()



time.sleep(3)
driver.close()
