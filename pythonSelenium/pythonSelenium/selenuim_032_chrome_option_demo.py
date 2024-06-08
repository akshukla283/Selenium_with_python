import time

from selenium import webdriver


# chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome option
chrome_options = webdriver.ChromeOptions()
# we can provide many option to chrome
chrome_options.add_argument("--start-maximized")
# headless execution take less time so nowadays people use it
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
# you can google for chrome options, you can refer below page
# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
# you can use user reason option to change usd rupees, and all

# now we have to pass the chrome option object
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)
# should return -->  GreenKart - veg and fruits kart
time.sleep(3)
# driver.close()
