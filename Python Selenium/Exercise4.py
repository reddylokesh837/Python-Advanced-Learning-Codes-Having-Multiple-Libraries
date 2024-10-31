import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




webdriverLocation = Service(executable_path="C:\\chromedriver.exe")



browser = webdriver.Chrome(service=webdriverLocation)
browser.get("https://www.google.com")
browser.maximize_window()


print(browser.title)

login_name_element = browser.find_element(By.ID,"login")
password_element = browser.find_element(By.ID, "password")
login_button = browser.find_element(By.ID, "login")

login_name_element.send_keys("T7302")
password_element.send_keys("T7302*abc")
login_button.click()
time.sleep(2)


print(browser.title)

logout_button = browser.find_element(By.ID, "logout")
login_button.click()


browser.quit()

