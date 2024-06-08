import time
from selenium import webdriver

# Chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# need to compare expected list to actual list
expected_prod_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_prod_list = []

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)  # why we didn't remove this time.sleep

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0  # if result less than 0 means there is glitch in web
print(count)


for result in results:
    # get the product name
    actual_prod_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

# 1- assignment done
assert expected_prod_list == actual_prod_list

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
# you got web element only, now you have to eaxract
sum = 0
for price in prices:
    sum += int(price.text)

print(f"Total sum : {sum}")
# finding total value to validate

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount
print(f"Validation successful\nExpected : {totalAmount}\nActual : {sum}")


# Next step apply promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
# Now to click apply button
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#
wait = WebDriverWait(driver, 10)
# we have to wait until the particular CSS_locator visible present
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))


print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# assignment 2 validate discount value

discountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAmount > discountAmount
print("Validation successful!")





# This will fail because web is taking time to load, so we can't use time.sleep every where

time.sleep(3)
# driver.close()
