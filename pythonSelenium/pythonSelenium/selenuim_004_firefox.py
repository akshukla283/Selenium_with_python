import time

from selenium import webdriver

# from selenium.webdriver.chrome.service import Service
# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# Firefox driver
driver = webdriver.Firefox()
driver.get("https://www.w3schools.com/python/")
driver.maximize_window()
print(driver.title)
print("Current url: ")
print(driver.current_url)