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

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0  # if result less than 0 means there is glitch in web
print(count)

# now to add item into cart click on add cart button
# we will use "chaining here
# in 'result' Xpath we have till //div[@class='products']/div/
# and for add cart button Xpath we have
# //div[@class='products']/div/div/button
# so for add cart button we can use 'result' xpath and then from there we can add some
# pending path "div/button"
for result in results:
    result.find_element(By.XPATH, "div/button").click()
    # now here find_element will search only for "ber" search item
# Now we have to check our cart

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# Next step apply promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
# Now to click apply button

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(3)
# Now after clicking apply button we have to validate whether it worked properly or not
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# This will fail because web is taking time to load, so we can't use time.sleep every where

time.sleep(3)
# driver.close()
