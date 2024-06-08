import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# some place due to VPN downloading drive got fail, so it can't communicate
# in that case manually download and pass the path
# first we have to check version of chrome and then download the same version driver
# go to chrome browser setting check version
# there is 'service' class in which we have pass the driver path
# always use "\\" for path in windows
service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome()
# Which url you want to open
driver.get("https://www.google.com")




# driver invoke browser very fast we can wait for some time
time.sleep(2)
