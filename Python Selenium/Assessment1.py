import time
import unittest
from fastapi import security
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC


"""
Create a new python unit test module "Exercise09_Login.py" inside the "UnitTesting" package of "Exercises_Selenium" Project.

In the SetUp method:

Open the AUT
Maximize the window
In the TearDown method:

Close the application
In the Test method:

Fetch the page title and print in the console as "Title of the page before login: <<Page Title>>"
Login to the application with Login Name: T7302  and Password: T7302*abc
Fetch the page title and print in the console as "Title of the page after login: <<Page Title>>"
Logout from the application
"""




class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # selecting webdriver
        webdriverLocation = Service(executable_path="C:\\chromedriver.exe")
        # initiating instance
        cls.browser = webdriver.Chrome(service=webdriverLocation)
        cls.browser.get("http://10.82.48.225:8081/EDUBank/tellerLogin/")


    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()


    def test_login(self):
        title_before = self.browser.title
        print(title_before)

        self.browser.find_element(By.ID,"loginbutton").click()
        self.browser.find_element(By.ID,"username").send_keys("lokesh")
        self.browser.find_element(By.ID,"password").send_keys("password")
        self.browser.find_element(By.ID,"submit").click()

        WebDriverWait(self.browser, 10).until(
            EC.title_contains("Home")
        )

        title_after = self.browser.title
        print(title_after)

        self.browser.find_element(By.ID,"Logout").click()



if __name__ == "__main__":
    unittest.main()