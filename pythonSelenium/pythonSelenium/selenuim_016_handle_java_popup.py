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

name = "Ankit"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
# if we click alert then only we will get popup message How do we get
# from driver mode to alert mode , we can achieve by "driver.switch_to.alert"
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
# we want to validate aur name test whether is it present in our popup message
assert name in alertText
print(f"Yes your name : {name} is there")


# Now you want to click on okay button
alert.accept()   # "accept" is method to click on okay
# there is another method "dismiss" this is to cancel the alert popup
# but in this example there is only 'ok' popup so we are blindly calling accept
# alert.dismiss()

time.sleep(3)
# driver.close()
