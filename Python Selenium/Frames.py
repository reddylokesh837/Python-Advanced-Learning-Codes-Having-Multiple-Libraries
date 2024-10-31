import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC

"""
Test Steps:

Launch the browser & open the "DemoApps" application.
Click on the frames link.
Fetch the below text of centre image 
Assert the text with "Infosys Mysore - GEC2 - Library"
Close the webdriver
 
"""

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
    
    def testFrames(self):
        self.browser.find_element(By.LINK_TEXT,"frames" ).click()
        text_center = self.browser.find_element(By.XPATH,"//*[@id='form1']/div[3]/div[2]/div/span").text
        assert "Infosys Mysore - GEC2 - Library" in text_center

        frames = WebDriverWait(self.browser,10).until(
            EC.frame_to_be_available_and_switch_to_it(0)
        )

        self.browser.find_element(By.ID,"input_field").send_keys("Input in frame")

        self.browser.switch_to.default_content()


        self.browser.switch_to.frame("Frame Id or Frame name")

        self.browser.find_element(By.ID,"another input field").send_keys("More input in another form")

        self.browser.switch_to.parent_frame()


        # by using the name of frame
        self.browser.switch_to.frame("center")

        # by using the id of frame
        self.browser.switch_to.frame("id1")

        # by using the index of frame
        self.browser.switch_to.frame(0)

        # by using the web element of frame
        # after identifying the number of frame tags, we can iterate the frames with the index of the tag
        frame_tags = self.browser.find_elements(By.TAG_NAME, "frame")
        for index in range(len(frame_tags)):
            self.browser.switch_to.default_content()
            frame = self.browser.find_elements(By.TAG_NAME,"frame")[index]
            self.browser.switch_to.frame(frame)

        # switching to parent content
        self.browser.switch_to.default_content()

        # handling alert
        alert = WebDriverWait(self.browser,10).until(EC.alert_is_present())
        alert.dismiss()
        alert.send_keys("lokesh")
        print(alert.text)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()