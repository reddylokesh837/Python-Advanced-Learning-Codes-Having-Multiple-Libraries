import time
import unittest
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
        # Initialize the WebDriver
        cls.browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        cls.browser.maximize_window()
        cls.browser.get("http://10.67.89.41/Automation/PSRestuarant/")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    def fetchValues(self, dropdownId):
        dropDown = Select(self.browser.find_element(By.ID, dropdownId))
        options = dropDown.options
        for option in options:
            if option != "--Select--":
                print(option.text)

    def testA(self):
        # Click on "Order Now" link
        self.browser.find_element(By.LINK_TEXT, "Order Now").click()

        # Click on 'Home Delivery' link
        self.browser.find_element(By.LINK_TEXT, "Home Delivery").click()     

        type_dropdown = Select(self.browser.find_element(By.ID,"type_dropdown"))
        type_dropdown.select_by_visible_text("Vegetarian")

        print("Veg Maindishes")
        self.fetchValues("maindish")

        print("veg curries")
        self.fetchValues("curry")

        self.browser.refresh()

        time.sleep(1)


        non_veg_dropdown = Select(self.browser.find_element(By.ID,"type_dropdown"))
        non_veg_dropdown.select_by_visible_text("Non-Vegetarian")

        print("Non-Veg Maindishes")
        self.fetchValues("maindish")

        print("Non-veg curries")
        self.fetchValues("curry")


        # Select Non-Veg Main Dish and Curry because the current selected dropdown is non_veg
        main_dish_dropdown = Select(self.browser.find_element(By.ID, "mainDish"))
        main_dish_dropdown.select_by_visible_text("roti Dish")  # Replace with actual dish name

        curry_dropdown = Select(self.browser.find_element(By.ID, "curry"))
        curry_dropdown.select_by_visible_text("chicken curry")  # Replace with actual curry name



        # Enter personal details
        self.browser.find_element(By.ID, "name").send_keys("Lokesh Reddy")
        self.browser.find_element(By.ID, "address").send_keys("123 Main St")
        self.browser.find_element(By.ID, "mobile").send_keys("9876543210")
        self.browser.find_element(By.ID, "email").send_keys("lokesh@example.com")

        # enter the coupon details
        self.browser.find_element(By.ID, "coupon").send_keys("COUPON10")

        # Uncheck the 'Send me receipt to Email & Mobile'
        self.browser.find_element(By.ID, "sendReceipt").click()

        # Click on submit button
        self.browser.find_element(By.ID, "submit").click()

        # Fetch and print the popup message
        alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert_message = alert.text
        print(f"Popup Message: {alert_message}")

        # Accept the alert
        alert.accept()









