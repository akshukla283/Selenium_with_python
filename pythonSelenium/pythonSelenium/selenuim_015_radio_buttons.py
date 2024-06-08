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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# our goal to select option from multiple item from checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        print("Option selected")
        break
# this time by using CSS selector

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[1].click()

assert radiobuttons[1].is_selected()

# checking any content is displayed or not

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
print("Yes it worked")

time.sleep(3)
driver.close()
