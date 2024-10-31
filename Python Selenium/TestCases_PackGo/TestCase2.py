import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from BaseClass import BaseClass
from selenium.webdriver.common import by



def tearDownModule():
    BaseClass.browser.close()
    BaseClass.browser=None

class SignUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        BaseClass.browser.maximize_window()
        time.sleep(3)
        BaseClass.browser.find_element(By.ID, "Logout").click()
        BaseClass.browser.refresh()
    
    def test_Signup(self):
        BaseClass.browser.find_element(By.ID, "Signup").click()
        BaseClass.browser.find_element(By.ID, "username").send_keys("username")
        BaseClass.browser.find_element(By.ID, "email").send_keys("email")
        BaseClass.browser.find_element(By.ID, "password").send_keys("password")
        BaseClass.browser.find_element(By.ID, "Signup").click()


        # Assertion 4: Verify success message after signup
        success_signup = BaseClass.browser.find_element(By.ID, "signUpSuccessMessage").text
        self.assertEqual(success_signup, "SignupSuccessful", "Signup was not successful")

        BaseClass.browser.find_element(By.ID, "closesignup").click()


