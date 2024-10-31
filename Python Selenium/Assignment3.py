"""Test Steps: 

Create a new python module "Exercise05_TakeAway.py" inside the "WebElementInteractions_Part1" package of "Exercises_Selenium" project
Open the AUT
Maximize the window
Click on Take Away link
Select Type as "Vegetarian"
Fetch and print all the values except "--Select--" from maindish and curry dropdown
Refresh the page.
Select Type as "Non-Vegetarian"
Fetch and print all the values except "--Select--" from maindish and curry dropdown
Close the application
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





browser.find_element(By.LINK_TEXT, "Take away link").click()





type_dropdown = Select(browser.find_element(By.ID,"type_dropdown"))
type_dropdown.select_by_visible_text("Vegetarian")



def fetchValues(dropdown_id):
    dropdown = Select(browser.find_element(By.ID,dropdown_id))
    options = dropdown.options
    for option in options:
        if option != "--Select--":
            print(option.text)


print("Veg Maindishes")
fetchValues("maindish")

print("veg curries")
fetchValues("curry")


browser.refresh()

time.sleep(1)




nonveg_type = Select(browser.find_element(By.ID,"typedropdown"))
nonveg_type.select_by_visible_text("Non-Vegetarian")

print("Non-Veg Maindishes")
fetchValues("maindish")


print("Non veg curries")
fetchValues("curries")


browser.close()