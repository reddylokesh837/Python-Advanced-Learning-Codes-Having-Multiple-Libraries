'''
Created on 23 Sept 2024

@author: reddy
'''
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



def setUpModule():
    # initializing the necessary browser element
    webdriverLocation = Service(executable_path="C:\\chromedriver.exe")
    BaseClass.browser = webdriver.Chrome(service=webdriverLocation)


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls)->None:
        BaseClass.browser.implicitly_wait(10)
        BaseClass.browser.get("https://www.google.com")
        BaseClass.browser.maximize_window()
        
    def test_Login(self):
        # login to the application
        BaseClass.browser.find_element(By.LINK_TEXT,"Login").click()
        BaseClass.browser.find_element(By.ID,"usernamelogin").send_keys("username")
        BaseClass.browser.find_element(By.ID,"password").send_keys("password")
        BaseClass.browser.find_element_by_id("login").click()

        # Assertion 1: Check if the user has navigated to the homepage
        home_element = BaseClass.browser.find_element(By.ID,"homepageElement")
        self.assertTrue(home_element.is_displayed(), "Failed to navigate to the home page afterlogin")

       
    def test_booking(self):
        time.sleep(2)
        # select the from destination dropdown
        sourceDropdown = Select(BaseClass.browser.find_element(By.ID,"fromDD"))
        # and then select by value
        sourceDropdown.select_by_value("Bengaluru")
        
        # then select the to destination dropdown
        destDropdown = Select(BaseClass.browser.find_element(By.ID,"toDD"))
        # then select by value
        destDropdown.select_by_value("Hyderabad")
        
        
        # find and click the search buses by the details you provided above
        BaseClass.browser.find_element(By.ID,"searchBus").click()
        # now wait for the table to load all the buses list with explicit 10seconds
        table = WebDriverWait(BaseClass.browser, 10).until(
            EC.presence_of_element_located((By.ID,"mytable")))
        # then find your preferred bus in the row
        row = table.find_element(By.ID,"thirdrow")
        # then choose the pickup point
        Select(row.find_element(By.ID,"fromDD2")).select_by_index(0)
        # then choose the drop point
        Select(row.find_element(By.ID, "toDD2")).select_by_index(1)
        # select the bus slot row
        row.find_element(By.XPATH,"\\[@id='radio3]").click()
        
        # once you select everything then proceed to book
        BaseClass.browser.find_element(By.ID,"book").click()


        # Assertion 2: Verify that the source and destination on the payment page match the selected options
        selected_source = BaseClass.browser.find_element(By.ID,"selectedsource").text
        selected_dest = BaseClass.browser.find_element(By.ID,"selecteddest").text
        self.assertEqual(selected_source, "Bengaluru", "Source does not match the selected value")
        self.assertEqual(selected_dest, "Hyderabad","Destination does not match the selected value")

        
        
        # fill in the no of passengers
        passengers = BaseClass.browser.find_element(By.ID,"counter")
        # clear the passengers
        passengers.clear()
        passengers.send_keys("2")
        passengers.send_keys(Keys.ENTER)
        
        
        BaseClass.browser.find_element(By.XPATH,"\\").click()
        
        BaseClass.browser.find_element(By.ID,"confirmbooking").click()
        
        # Assertion 3: Verify the success message after booking
        success_message = BaseClass.browser.find_element(By.ID,"successMessage").text
        self.assertEqual(success_message, "Booking Successful!", "Booking was not successful!")

        time.sleep(2)
        
        # accept the alert
        BaseClass.browser.switch_to_alert().accept()
        #BaseClass.browser.find_element_by_link_text("LogOut").click()
            
