import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 360)




driver.get("https://www.saucedemo.com/")

actions = ActionChains(driver) 

email = driver.find_element_by_xpath(
    "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input"
)
time.sleep(1)
email.send_keys("standard_user")
actions.send_keys(Keys.TAB)
actions.send_keys("secret_sauce")
actions.send_keys(Keys.ENTER)
actions.perform()

time.sleep(10)

driver.quit()