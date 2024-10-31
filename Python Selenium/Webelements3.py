
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common import by
import unittest

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # selecting webdriver
        webdriverLocation = Service(executable_path="C:\\chromedriver.exe")
        # initiating instance
        cls.browser = webdriver.Chrome(service=webdriverLocation)
        # launch the application
        cls.browser.get("https://www.google.com")
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.find_element(By.ID,"Logout Button").click()
        cls.browser.close()
    
    def testA(self):
        self.browser.find_element(By.NAME,"login").click()
        self.browser.find_element(By.ID,"username").send_keys("lokesh")
        self.browser.find_element(By.ID,"password").send_keys("password")
        self.browser.find_element(By.ID,"login").click()
        
        # so whenever we want to enter something should use send_keys
        self.browser.find_element(By.ID,"from_date").send_keys("11/12/2018")
        self.browser.find_element(By.ID,"to_date").send_keys("11/12/2019")

        # click View Transactions
        time.sleep(3)


        transactions = self.browser.find_elements(By.XPATH,"//tr")
        for transaction in transactions:
            columns = transaction.find_elements(By.ID,"td")
            for column in columns:
                print("Transaction details",column[0].text)
        
        self.assertIn(self.browser.title)



if __name__ == "__main__":
    unittest.main()
