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
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
    
    def testFrames(self):
        self.browser.find_element(By.LINK_TEXT,"frames" ).click()
        
        frame_tags = self.browser.find_elements(By.TAG_NAME,"frame")
        text_list=[]
        for index in range(len(frame_tags)):
            self.browser.switch_to.default_content()

            frame = frame_tags[index]
            self.browser.switch_to.frame(frame)


            # fetch the text below the image inside the current frame
            text_element = WebDriverWait(self.browser,10).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Infosys')]"))
            )

            text_list.append(text_element.text)

        self.browser.switch_to.default_content()

        # Assert that one of the texts contains "Infosys Mysore"
        found_infosys = any("Infosys Mysore" in text for text in text_list)
        self.assertTrue(found_infosys,"The infosys mysore text in not present below the images")