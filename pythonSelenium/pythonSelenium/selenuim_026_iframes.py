import time

from selenium import webdriver
from selenium.webdriver import ActionChains

# chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

# we need to switch to frame because driver is unable to locate element ID
# so whenever there is frame in HTML then we need to switch to frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()   # to clear something present alread
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

# to automate outside to frame, need to switch back to original
# I mean normal browser scope
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)



time.sleep(3)
# driver.close()
