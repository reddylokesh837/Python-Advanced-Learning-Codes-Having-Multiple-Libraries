
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common import by
import unittest


class Test(unittest.TestCase):
    application_under_test = "https://www.google.com"
    webdriverLocation = Service(executable_path="C:\\chromedriver.exe")

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(service=self.webdriverLocation)
        self.browser.maximize_window()
    
    def tearDown(self) -> None:
        self.browser.close()
    
    def testA(self):
        self.browser.find_element(By.LINK_TEXT,"About Us").click()

        wind_hanlde = self.browser.window_handles
        print(len(wind_hanlde))

        for handle in wind_hanlde:
            self.browser.switch_to.window(handle)
            print(self.browser.current_url)

        paragraph1 = self.browser.find_element(By.XPATH,"//p[@value='about us details']").text

        print("About us details", paragraph1)

if __name__=="__main__":
    unittest.main()
