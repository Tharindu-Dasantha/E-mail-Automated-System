import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# debug reasons
import sys

driver = webdriver.Chrome()
actions = ActionChains(driver) 
wait = WebDriverWait(driver, 360)


# Open the browser & go to the zoho mail
Zoho_url = "https://accounts.zoho.com/signin?servicename=VirtualOffice&signupurl=https://www.zoho.com/mail/zohomail-pricing.html&serviceurl=https://mail.zoho.com"
driver.get(Zoho_url)

# Handling the email page
email_adress = driver.find_element_by_xpath(
    "/html/body/div[4]/div[1]/div[3]/div[3]/form[1]/div[2]/div[1]/div/span/input")
email_adress.send_keys("hello@creativo-code.com")
email_button = driver.find_element_by_xpath(
    "/html/body/div[4]/div[1]/div[3]/div[3]/form[1]/button")
email_button.click()

# Waiting till the password bar appears
input_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
input_field.send_keys("lab@creativocode")
signin_button = driver.find_element_by_xpath(
    "/html/body/div[4]/div[1]/div[3]/div[3]/form[1]/button")
signin_button.click()

# Sending email to the end of the list
email_file = open("email.txt", "r")
lines = email_file.readlines()
for line in lines:
    email = line.strip()
    # sending the email using the given email address
    # Waiting until the page is loaded
    newMailButton = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/button[1]")))

    for i in range(1, 21):
        print(i)
        time.sleep(1)

    mailbutton = driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/button[1]")
    mailbutton.click()

    print("Tring to send a mail to " + email)
    # Wait till the send page is loaded
    send_button = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[1]/button[1]")))

    for i in range(1, 11):
        print(i)
        time.sleep(1)
    print("creating a new mail for " + email)

    TOField = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[4]/div[1]/div/input")))
    TOField.send_keys(f"{email}")
    

    subject = driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[5]/input")
    subject.send_keys("just a test")  # the subject for the email

    
    actions.send_keys(Keys.TAB)
    actions.send_keys("Just testing wheather this works")
    actions.perform()
    
    input()

    # body = driver.find_element_by_class_name("ze_body")
    # body.send_keys("hello there")  # the body for the email

    for i in range(1, 10):
        print(i)
        time.sleep(1)

    send_button.click()

driver.quit()