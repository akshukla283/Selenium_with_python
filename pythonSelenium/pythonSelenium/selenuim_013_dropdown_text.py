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

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# we are going to select text based on popup shown by passing some word
# so we have to wait at least 2 second to show popup
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)  # sleeping for two minute so that by the time option
# you can choose which option you have to take just inspect that
# as we can sse after doing inspect there three options
# ID, Class, Tabindex

# this time we used 'find_elements' instead of 'find_element' which will iterator over all the select items
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
# this variable "countries" will store list of countries
print(len(countries))

for country in countries:
    if country.text == "India":  # country.text (extract web element text)
        country.click()
        break   # if condition satisfied then we can break the loop

# for validation purpose we can extract that word
# print(driver.find_element(By.ID, "autosuggest").text)  # here used 'find_element'
# above text can't retrieve by .text method as when website load there was no text
# to get that we will use new method
# ".get_attribute("value")"
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
# now we can make assertion
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
print("Successfully validated")

time.sleep(3)
driver.close()
