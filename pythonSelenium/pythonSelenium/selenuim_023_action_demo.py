import time
from selenium import webdriver
from selenium.webdriver import ActionChains

# Chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Class ActionChains in this we have to send driver as object

action = ActionChains(driver)
# to execute this action we need to use 'perform()' at end

# right click
# action.context_click()
# double click
# action.double_click()
# action.click_and_hold()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# to reload
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

# note for Xpath and CSS we can validate or search
# through console for
# Xpath > $x("//button[@class='btn btn-success']")
# CSS  -> $("button[class='btn btn-success']")

time.sleep(3)
# driver.close()
