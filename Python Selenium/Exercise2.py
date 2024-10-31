import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



webdriverLocation = Service(executable_path="C:\\chromedriver.exe")

browser = webdriver.Chrome(service=webdriverLocation)

browser.get("https://www.google.com")
browser.maximize_window()
print(browser.current_url)
print(browser.title)
time.sleep(2)
browser.quit()



