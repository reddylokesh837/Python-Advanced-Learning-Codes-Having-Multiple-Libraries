import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from Login.Login import LoginPage
from Pages.Homepage import HomePage
import time

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        executablePath = "D:\\chromedriver.exe"
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        cls.driver.close()

    def testMethod(self):
        driver =self.driver
        driver.get("https://www.google.com")


        Home = HomePage(driver)
        Home.LoginClick(driver)

        login = LoginPage(driver)
        login.EnterUsername("lokesh")
        login.EnterPassword("password")
        login.LoginAUT()
        print(driver.title)




if __name__ == "__main__":
    unittest.main()