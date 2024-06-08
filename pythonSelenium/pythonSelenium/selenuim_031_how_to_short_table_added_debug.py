import time

from selenium import webdriver


# chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")


browserSortedVeggies = []
# we can make Xpath using text in side that
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# this time we want to catch every thing in list, so will use plural
veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
# collect all veggie name -> BrowserSortedveggieList (A, B, C)

# to debug it we neet to mark break point by clicking on line and runas debug mode

for element in veggieWebElement:
    browserSortedVeggies.append(element.text)

OriginalBrowserSortedList = browserSortedVeggies.copy()

# now sorting the web list
browserSortedVeggies.sort()

assert browserSortedVeggies == OriginalBrowserSortedList
# if any changes will be there after using Sorted then it will fail
print("Comparison is successfully done")


time.sleep(3)
# driver.close()
