"""
Test Steps: 

Create a new python module "Exercise05_AddCustomer.py" inside the "WebElementInteractions_Part1" package of "Exercises_Selenium" project
Open the AUT
Maximize the window
Login to the application
Enter Name, Email Id and Date of Birth
Select the security question as "What was the name of your first pet?"
Enter the security answer.
Click on Add Customer
Logout from the application
 """


import time
from fastapi import security
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


# selecting webdriver
webdriverLocation = Service(executable_path="C:\\chromedriver.exe")
# initiating instance
browser = webdriver.Chrome(service=webdriverLocation)

# Open the AUT
browser.get("https://www.google.com")

# maximizing the window
browser.maximize_window()

# login to the details
browser.find_element(By.ID,"username").send_keys("Lokesh")
browser.find_element(By.ID,"password").send_keys("Lokeshreddy")
browser.find_element(By.ID,"login button").click()


# Enter Name, Email Id and Date of Birth
browser.find_element(By.ID,"name").send_keys("lokesh reddy")
browser.find_element(By.ID,"Email Id").send_keys("reddylokesh837@gmail.com")
browser.find_element(By.ID,"dob").send_keys("DATE OF BIRTH")

# selecting the security question
securityQuestion = browser.find_element(By.ID,"Select Dropdown")
dropDown = Select(securityQuestion)
dropDown.select_by_value("What was the name of your first pet?")

# Enter the security answer.
browser.find_element(By.LINK_TEXT, "What was the name of your first pet?")


# Click on Add Customer
browser.find_element(By.ID,"Add Customer").click()

time.sleep(2)

# Logout from the application
browser.find_element(By.ID, "Logout").click()

# Close the AUT Application Under Test
browser.close()



