import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 360)

# Opening the files to read and write
filename = input("Enter the file name with the txt: ")
filewiththefblink = "Website/Facebook/" + filename
FBlink = open(filewiththefblink)
filetosavetheEmail = "Website/EmailAddress/" + filename
EmailAddress = open(filetosavetheEmail, "w")
filetosavethePhoneNumber = "Website/Phonenumbers/" + filename
PhoneNumber = open(filetosavethePhoneNumber, "w")   

# opening the each facebook file
lines = FBlink.readlines()
for line in lines:
    # Open the fb page
    link = line.strip()
    driver.get(link)
    
    # get the name of the company
    
    
    # if it have a email address save it to the email address file 