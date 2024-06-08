import time
from selenium import webdriver

# Chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()

# this time another website

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# after typing in search box it will take few seconds to load
time.sleep(2)
# after entering son search word there many option then
# we should use find_elements plurals so that we can iterate through option
# if we want count of the object we should write locator like for find_elements plural

result = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(result)

assert count > 0  # if result less than 0 means there is glitch in web
print(count)

# now to add item into cart click on add cart button





time.sleep(3)
# driver.close()
