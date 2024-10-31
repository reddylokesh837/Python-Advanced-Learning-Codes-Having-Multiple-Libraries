import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC



class AddCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # selecting webdriver
        webdriverLocation = Service(executable_path="C:\\chromedriver.exe")
        # initiating instance
        cls.browser = webdriver.Chrome(service=webdriverLocation)
        cls.browser.get("https://www.google.com")
        cls.browser.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.find_element(By.LINK_TEXT,"Logout").click()
        cls.browser.close()


    def test_Login(self):
        title_before = self.browser.title
        print(title_before)
        self.browser.find_element(By.ID,"username").send_keys("T7302")
        self.browser.find_element(By.ID,"password").send_keys("T7302*abc")
        self.browser.find_element(By.ID,"login").click()


        WebDriverWait(self.browser,10).until(
            EC.title_contains("Customer")
        )

        title_after = self.browser.title
        print(title_after)

        # assertion whether title is loaded or not
        self.assertIn("Customer", title_after, "Title is not there!")


    def testAdd(self):
        # self.test_Login() Not recommended

        # Navigate to the customer page
        self.browser.find_element(By.ID, "Add Customer").click()    

        # fill in the customer details
        self.browser.find_element(By.ID, "name").send_keys("Lokesh")
        self.browser.find_element(By.ID, "email").send_keys("Lokesh@123")
        self.browser.find_element(By.ID, "dob").send_keys("01/01/2000")

        # Assertion
        self.assertIn("01/01/2000", self.browser.find_element(By.ID, "dob").get_attribute("value"))

        # select the security question
        securityDropdown = Select(self.browser.find_element(By.NAME,"securityQuestion"))
        securityDropdown.select_by_visible_text("What was the name of your first pet?")


        # enter the security answer
        self.browser.find_element(By.ID,"security answer").send_keys("Gymmy is my dog")

        # assertion equal
        self.assertEqual("Gymmy is my dog", self.browser.find_element(By.ID,"security answer").get_attribute("value"))


        # click on add customer
        self.browser.find_element(By.NAME,"Add Customer").click()

        # success message
        success_message = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'success')]"))
        )
        print(success_message)


"""
In the Test_customer_add method:

Enter Name, Email Id and Date of Birth
Select the security question as "What was the name of your first pet?"
Enter the security answer.
Click on Add Customer

Expected output:

The webdriver which login to the application, the same driver needs to act on the "add customer" page.
"""

    
