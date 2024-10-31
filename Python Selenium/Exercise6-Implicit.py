
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.service import Service




webdriverLocation = Service(executable_path="C:\\chromedriver.exe")

browser = webdriver.Chrome(service=webdriverLocation)

# create an implicit wait in seconds
browser.implicitly_wait(10)

browser.get("https://www.google.com")




browser.find_element(By.LINK_TEXT, "Login").click()



browser.find_element(By.ID,"username").send_keys("Lokesh")
browser.find_element(By.ID,"password").send_keys("password")
browser.find_element(By.ID,"login").click() 

browser.find_element(By.ID,"logout").click()


