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



"""
Test Steps:

Launch the browser & open the "HMS" application.
Log in to the application.
Select the "patient" link from the main menu.
Select the "case file" link from the sub-menu and click on the link.
Log out from the application 
Close the webdriver.
Implementation of the above test steps is discussed in the upcoming pages.

"""


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Initialize the WebDriver
        cls.browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        cls.browser.maximize_window()
        cls.browser.get("http://10.67.89.41/Automation/PSRestuarant/")
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    
    def testApp(self):
        self.browser.find_element(By.ID,"txtUserID").send_keys("11")
        self.browser.find_element(By.ID,"txtPassword").send_keys("lokesh")
        self.browser.find_element(By.ID,"btnlogin").click()


        first_patient = self.browser.find_element(By.XPATH,f"//[@id='first']")
        second_patient = self.browser.find_element(By.XPATH,f"//[@id='first']")

        actions = ActionChains(self.browser)
        actions.move_to_element(first_patient)
        actions.click(second_patient)
        actions.perform()

        self.browser.find_element(By.LINK_TEXT,"logout").click()



if __name__ == "__main__":
    unittest.main()






