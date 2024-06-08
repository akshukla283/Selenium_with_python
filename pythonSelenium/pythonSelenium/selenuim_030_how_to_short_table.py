import time

from selenium import webdriver


# chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# click on column header

# we can make Xpath using text in side that
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# this time we want to catch every thing in list, so will use plural
veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
# collect all veggie name -> BrowserSortedveggieList (A, B, C)
browserSortedVeggies = []
for element in veggieWebElement:
    browserSortedVeggies.append(element.text)

# Sort this veggieList => newSortedList
# BrowserSortedveggieList == newSortedList
# now sort these elements again
# we can compare by sorted method after again sort of web element
# we can achieve this by using two method
# 1-> make copy of web veggie list and sort the original list and compare
# 2-> of directly use sorted method and compare
assert browserSortedVeggies == sorted(browserSortedVeggies)
# if any changes will be there after using Sorted then it will fail
print("Comparison is successfully done")


time.sleep(3)
# driver.close()
