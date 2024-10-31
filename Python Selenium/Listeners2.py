import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common import by
from Listeners import Listener

from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.ef_browser = webdriver.Chrome("//path")
        self.browser = EventFiringWebDriver(self.ef_browser,Listener())
        self.browser.get("https://www.google.com")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.browser.quit()
    
    def testLogin(self):
        self.browser.find_element(By.LINK_TEXT,"login").click()
        self.browser.find_element(By.ID,"username").send_keys("lokesh")
        self.browser.find_element(By.ID,"password").send_keys("password")
        self.browser.find_element(By.ID,"login").click()

        wait = WebDriverWait(self.browser,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='fromDD']/option[contains(text(),'Hyderabad')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='toDD']/option[contains(text(),'Bengaluru')]"))).click()
        wait.until(EC.element_to_be_clickable((By.ID,"searchbus"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='radio3']"))).click()
        wait.until(EC.element_to_be_clickable((By.ID,"book"))).click()

        passengers = self.browser.find_element(By.ID,"counter")
        passengers.clear()
        passengers.send_keys("2")

        self.browser.find_element(By.ID,"calculateBillButton").click()
        self.browser.find_element(By.ID,"confirmbooking").click()
        self.browser.switch_to.alert.accept()


class MyTestResult(unittest.TestResult):
    def startTest(self, test: unittest.TestCase) -> None:
        super().startTest(test)
        print(f"Starting test: {test}")


    def stopTest(self, test: unittest.TestCase) -> None:
        super().stopTest(test)
        print(f"Stopping test: {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"Test failed: {test}")

    def addSuccess(self, test: unittest.TestCase) -> None:
        super().addSuccess(test)
        print(f"Test passed: {test}")

    def addSkip(self, test: unittest.TestCase, reason: str) -> None:
        super().addSkip(test, reason)
        print(f"Test skipped: {test}")
        
    def addExpectedFailure(self, test, err):
        super().addExpectedFailure(test, err)
        print(f"Expected Failure: {test}")
        print(f"Error: {err}")

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        print(f"Unexpected Success: {test}")



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    result = MyTestResult()
    suite.run(result)