from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC


class HomePage():
    def __init__(self,driver) -> None:
        self.driver = driver
        self.loginlink = "Login"

    def LoginClick(self,driver):
        self.driver.find_element(By.LINK_TEXT,self.loginlink).click()