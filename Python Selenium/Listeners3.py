import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common import by
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

import HtmlTestRunner
# from HtmlTestRunner import runner
# from HtmlTestRunner.runner import HTMLTestRunner


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver) -> None:
        print(f"Before find: Finding element by {by} and value {value}")

    def before_click(self, element, driver) -> None:
        print("Before clicking on", element)
    
    def after_navigate_to(self, url: str, driver) -> None:
        print("After navigating to:", url)
    
    def after_close(self, driver) -> None:
        print("After closing the browser")

class PSRestaurantTest(unittest.TestCase):
    def setUp(self):
        self.ef_browser = webdriver.Chrome()
        self.browser = EventFiringWebDriver(self.ef_browser, MyListener())
        self.browser.get("https://www.psrestaurant.com/")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def tearDown(self) -> None:
        self.ef_browser.close()
        self.ef_browser.quit()
    
    def testNavigatiob(self):
        orderLink = self.ef_browser.find_element(By.ID,"menu-item-544966").click()

        aboutlink = self.ef_browser.find_element(By.ID,"menu-item-545773").click()

        page_title = self.ef_browser.title
        page_url = self.ef_browser.current_url

        print(f"Page title: {page_title}")
        print(f"Page url: {page_url}")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="demo/reports"))