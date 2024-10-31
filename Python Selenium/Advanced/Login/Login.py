
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC

class LoginPage():
    def __init__(self, driver) -> None:
        self.driver = driver
        self.username_id = "usernameLogin"
        self.password_id = "passwordLogin"
        self.login_id = "login"

    def EnterUsername(self,username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def EnterPassword(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def LoginAUT(self):
        self.driver.find_element(By.ID,self.login_id).click()