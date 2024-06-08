import time
from selenium import webdriver
# Chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
# we are landing on another url https://rahulshettyacademy.com/client
driver.get("https://rahulshettyacademy.com/client")
# some locators - ID, Xpath, CSSSelector, 'Classname', name, linkText
# based on linkText we can Identify the locators
# for example "forgot password", we have to confirm it by checking html anchor tag
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# we can use "PARTIAL_LINK_TEXT" instead of LINK_TEXT will work same, then we can give on "forgot" it will detect
# now you will land on another page from where you have to select email and password
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# in password, we will use "CSS" locator in that instead of "/" use space
# form div:nth-child(2) input
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
# now need to confirm password in another tab
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
# Xpath help to select any text ( if you don't have ny thing on page you can select tag based on test
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(3)
driver.close()
