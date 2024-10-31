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
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()


    def test_Login(self):
        self.browser.find_element(By.LINK_TEXT, "login").click()
        self.browser.find_element(By.ID,"usename").send_keys("lokesh")
        self.browser.find_element(By.ID, "password").send_keys("password")
        self.browser.find_element(By.ID,"login").click()

        patient_link = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Patient"))
        )
        self.assertTrue(patient_link.is_displayed())

    def TestB(self):
        # Assume user is already logged in by calling the testA login method
        self.TestA()

        # Hover over Patient link
        patient_link = self.browser.find_element(By.LINK_TEXT, "Patient")
        actions = ActionChains(self.browser)
        actions.move_to_element(patient_link).perform()

        obs_presc = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Observation Prescriptions"))
        )

        actions.move_to_element(obs_presc).click().perform()

        
        patient_id_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID,"patientID"))
        )
        patient_id_input.send_keys("11")

        self.browser.find_element(By.ID,"getPatientDetails").click()

        blood_group = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.ID,"bloodgroup"))
        )

        print(f"Patient blood group: {blood_group.text}")
        self.assertNotEqual(blood_group,"")

if __name__ =="__main__":
    unittest.main()