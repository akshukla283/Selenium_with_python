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

radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radiobuttons))
for radio_button in radiobuttons:
    if radio_button.get_attribute("value") == "radio2":
        radio_button.click()
        assert radio_button.is_selected()
        print("Radio button selected")
        break

time.sleep(3)
driver.close()
