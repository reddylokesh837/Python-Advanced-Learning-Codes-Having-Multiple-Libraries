import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




webdriverLocation = Service(executable_path="C:\\chromedriver.exe")


browser = webdriver.Chrome(service=webdriverLocation)
browser.get("https://www.google.com")
browser.maximize_window()
time.sleep(2)
browser.get_screenshot_as_file("customer.png")

browser.get("https://www.google.com")
time.sleep(2)
browser.get_screenshot_as_file("teller.png")

page_source = browser.page_source

print(len(page_source))
browser.quit()