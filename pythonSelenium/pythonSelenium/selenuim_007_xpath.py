import time

from selenium import webdriver

# If want to use service method for Chrome driver you can uncomment below import and giver downloaded driver path
# in windows always use "\\" in path
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
# //tagname[@attribute='value'] -> //input[@type='submit]

driver.find_element(By.XPATH, "//input[@type='submit']").click()
# after feeling the form some text will come we have to validate that too
# we can grab the success text
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

# time.sleep(3)