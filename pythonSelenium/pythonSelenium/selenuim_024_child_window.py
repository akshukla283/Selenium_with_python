import time
from selenium import webdriver
from selenium.webdriver import ActionChains

# Firefox

from selenium.webdriver.common.by import By


# service_obj = Service("D:\\drivers_selenium\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
# there is windows handler which store all open windows in list, we can retrieve by index
windowsOpened = driver.window_handles

# switch new windows
driver.switch_to.window(windowsOpened[1])  # will get child windows
print(driver.find_element(By.TAG_NAME, "h3").text)
# we can close that window as well
# driver.close()
# switch back to your parent windows
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, 'h3').text

time.sleep(3)
# driver.close()
