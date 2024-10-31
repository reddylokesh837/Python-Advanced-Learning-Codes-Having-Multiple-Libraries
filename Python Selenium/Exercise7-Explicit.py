from lib2to3.pgen2 import driver
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.service import Service

# for explicit wait we need to import these
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


webdriverLocation = Service(executable_path="C:\\chromedriver.exe")

browser = webdriver.Chrome(service=webdriverLocation)

browser.find_element(By.LINK_TEXT, "Login").click()

browser.find_element(By.ID,"username").send_keys("Lokesh")
browser.find_element(By.ID,"password").send_keys("password")
browser.find_element(By.ID,"login").click()


sourceDropdown = Select(browser.find_element(By.ID,"fromDD"))
sourceDropdown.select_by_value("Bengaluru")

destDropdown = Select(browser.find_element(By.ID,"toDD"))
destDropdown.select_by_value("Hyderabad")

#click on search bus button
browser.find_element(By.ID,"searchBus").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "travelTable"))
)


# select the bus slot row
radioButton = browser.find_element(By.XPATH,"//some-path")

browser.find_element(By.ID,"Book").click()

# print the current url of the page
print(browser.current_url)

# close the browser
browser.close()




