

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




webdriverLocation = Service(executable_path="C:\\chromedriver.exe")
browser = webdriver.Chrome(service=webdriverLocation)
browser.get("https://www.google.com")

browser.find_element(By.ID, "APjFqb").send_keys("Lokesh Reddy Vakada")
browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()

time.sleep(1)

browser.maximize_window()
browser.back()
time.sleep(1)

browser.forward()
time.sleep(1)

browser.refresh()
browser.get_screenshot_as_file("lokesh.png")

print(browser.title)
print(browser.current_url)
input("Enter your name")
