import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

exactfilename =input("Enter the filename with txt: ")
filename = "Website/outputs/" + exactfilename
urlfile = open(filename, 'r')

driver = webdriver.Chrome()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 360)


lines = set(urlfile.readlines())
for line in lines:
    # if re.match("https://", line):
    #     driver.get(line)
        
    #     driver.close()
    driver.get(line)
    facebookButton = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[4]/div[2]/div[3]/div/div/div[2]/div/li/a")))
    facebookButton.click()
    break