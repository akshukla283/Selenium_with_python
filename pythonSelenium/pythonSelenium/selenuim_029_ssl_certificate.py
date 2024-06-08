import time

from selenium import webdriver


# chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# sometimes you see ssl certificate
# this website is not trustable, proceed anyway by clicking in advance

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# then we need to set another option
chrome_options.add_argument("--ignore-certificate-errors")

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# we need to pass option argument to invoke execution in background
# if you will run this script you will not see any visible process, but automation
# will happen in background 
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# suppose we want scroll down  then to handle in python
# to do that we need to do inspect and then need to go console
# we can type javascript method over there
# window.scrollBy(0,document.body.scrollHeight)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# here execute_script know that the command is to execute in javascript
# if you want to scroll in middle just check that position and provide in method
# window.scrollBy(0,500)
# we can take screenshot also
driver.get_screenshot_as_file("screen.png")
# this file will be in you current folder


time.sleep(3)
# driver.close()
