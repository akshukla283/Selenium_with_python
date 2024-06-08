import time
from selenium import webdriver

# Chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# What is implicit wait --> it's type of global timeout

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# it will apply globally in code wherever it needed
# here implicitly_wait(5) means max timeout is 5 second
# if element displayed in 2 second then it immediately proceed for next step
# That is why we use this, if we use sleep method then it will sleep 5 seconds, no matter
# element got displayed in 2 seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)  # why we didn't remove this time.sleep
# because below we used special find_elements plural which return list
# whether it returns empty list which is still valid
# But we want actual list, so we sleep here this is only exception case
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0  # if result less than 0 means there is glitch in web
print(count)

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# Next step apply promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
# Now to click apply button
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# Now after clicking apply button we have to validate whether it worked properly or not
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# This will fail because web is taking time to load, so we can't use time.sleep every where

time.sleep(3)
# driver.close()
