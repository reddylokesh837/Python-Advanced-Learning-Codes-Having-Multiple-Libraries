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



class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        cls.browser.maximize_window()
        cls.browser.get("http://url_of_pack_and_go")  # Replace with the actual URL
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()

    def testTicketBooking(self):
        login_link = WebDriverWait(self.browser,10).until(
            EC.element_to_be_clickable((By.LINK_TEXT,"Login"))
        )
        login_link.click()

        username_field = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.ID,"username"))
        )
        username_field.send_keys("lokesh")

        password_field = WebDriverWait(self.browser,10).until(
            EC.visibility_of_element_located((By.ID,"password"))
        )
        password_field.send_keys("password")

        self.browser.find_element(By.ID, "loginButton").click()  # Replace with the actual login button ID

        source_dropdown = Select(self.browser.find_element(By.ID,"fromDD"))
        source_dropdown.select_by_visible_text("Bengaluru")

        dest_dropdown = Select(WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.ID,"destDropdown"))
        ))
        dest_dropdown.select_by_visible_text("Hyderabad")

        # for options

        source_options = source_dropdown.options
        for option in source_options:
            print(option.text)

        # for options

        dest_options = dest_dropdown.options
        for option in dest_options:
            print(option.text)


        self.browser.find_element(By.ID, "searchBusesButton").click()  # Replace with actual search button ID

        # Select a bus slot
        bus_slot = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='bus-slot'][1]"))  # Adjust XPath accordingly
        )
        bus_slot.click()


        # Select the radio button and click on proceed booking
        self.browser.find_element(By.XPATH, "//input[@type='radio']").click()  # Replace with the actual radio button selector
        self.browser.find_element(By.ID, "proceedBookingButton").click() 

        # enter the number of passengers
        passengersField = self.browser.find_element(By.ID,"passengerCount")
        passengersField.clear()
        passengersField.send_keys("2")

        # click on total bill
        self.browser.find_element(By.ID, "totalBill").click()

        # click on confirmbooking
        self.browser.find_element(By.ID, "confirmBookingButton").click()

        # fetch the alert message
        alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert_message = alert.text
        print(f"Alert message: {alert_message}")

        alert.accept()

        self.browser.find_element(By.XPATH,"html/body/div[2]/div[1]/div[2]/input").click()
        alert.dismiss()
        
        self.browser.find_element(By.XPATH,"html/body/div[2]/div[1]/div[3]/input").click()
        alert.send_keys("John")
        alert.accept()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()