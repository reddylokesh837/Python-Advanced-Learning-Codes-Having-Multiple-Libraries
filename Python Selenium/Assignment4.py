
"""
Test Steps: 

Create a new python module "Exercise07_Sync.py" inside the "WebElementInteractions_Part1" package of "Exercises_Selenium" project
Open the AUT
Maximize the window
Add an implicit wait of 1000 milliseconds
Login to the application by "Steven" as Login Name and "Steven!123" as a password.
Add an explicit wait for 5 seconds till the driver title is "Customer Home"
Logout from the application 
Close the application
"""


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# selecting webdriver
webdriverLocation = Service(executable_path="C:\\chromedriver.exe")
# initiating instance
browser = webdriver.Chrome(service=webdriverLocation)

browser.get("https://www.google.com")


browser.maximize_window()

browser.implicitly_wait(1)


browser.find_element(By.LINK_TEXT,"Login").click()

browser.find_element(By.ID,"username").send_keys("Steven")
browser.find_element(By.ID,"password").send_keys("Steven!123")

browser.find_element(By.ID,"login").click()

# here browser is the driver to wait
WebDriverWait(browser, 1000).until(
    EC.title_is("Customer Home")
)

browser.find_element(By.ID,"logout").click()

browser.close()





















