"""
Test Steps:

Launch the browser & open the "DemoApps" application.
Click on "Drag and Drop" link
Drag the "Drop me to my target" image and drop in the destination.
Assert the property of the destination after drop is done.
Close the webdriver.
Implementation of the above test steps is discussed in the upcoming pages."""




import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Initialize the WebDriver
        cls.browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        cls.browser.maximize_window()
        cls.browser.get("http://10.67.89.41/Automation/PSRestuarant/")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    def testA(self):
        self.browser.find_element(By.LINK_TEXT,"Drag and Drop").click()
        source = self.browser.find_element(By.ID,"droppable")
        target = self.browser.find_element(By.ID,"droppable")

        mouse = ActionChains(self.browser).drag_and_drop(source, target)
        mouse.perform()
        msg_after_drop = self.browser.find_element(By.XPATH, "//[@id='droppable]").text

        assert "Dropped" in msg_after_drop


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
