import time

from selenium import webdriver

# Chrome driver service
# first we will talk with driver to invoke
# At the time of Chrome release they release the same version driver as well
# some place due to VPN downloading drive got fail, so it can't communicate
# in that case manually download and pass the path


driver = webdriver.Chrome()
# Which url you want to open
driver.get("https://www.google.com")



# driver invoke browser very fast we can wait for some time
time.sleep(2)
