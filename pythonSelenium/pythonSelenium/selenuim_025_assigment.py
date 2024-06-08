import time
import re
from selenium import webdriver
from selenium.webdriver import ActionChains

# Chrome
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()
# to handle the all opened windows
windowsOpened = driver.window_handles
# switch new windows
driver.switch_to.window(windowsOpened[1])  # will get child windows
selected_text = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
print(selected_text)
email = [val for val in selected_text.split() if "@" in val][0]
print(email)
user_name = re.split("[.@]", email)[1]
print(user_name)
time.sleep(2)
# after selecting email switch back to parent window
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID, "username").send_keys(user_name)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.XPATH, "//input[@value='user']").click()
# after click to remove popup we have to wait till pop generate
# driver.implicitly_wait(5)  already used above
# to get popup
# alert = driver.switch_to.alert
# driver.find_element(By.CLASS_NAME, "btn btn-success").click()
driver.find_element(By.XPATH, "//button[text()='Okay']").click()

# static dropdown
dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
dropdown.select_by_visible_text("Student")
checkbox = driver.find_element(By.XPATH, "//input[@id='terms']")

driver.execute_script("arguments[0].click();", checkbox)
driver.find_element(By.XPATH, "//input[@value='Sign In']").click()



time.sleep(3)
# driver.close()
