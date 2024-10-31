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








import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener



class Listener(AbstractEventListener):
    def before_navigate_to(self, url: str, driver) -> None:
        print("Before navigating to:", url)
    
    def after_navigate_to(self, url: str, driver) -> None:
        print("After navigating to:", url)

    def before_click(self, element, driver) -> None:
        print("Before clicking on", element)
    
    def after_click(self, element, driver) -> None:
        print("After clicking on", element)
    
    def before_close(self, driver) -> None:
        print("Before closing the browser")

    def after_close(self, driver) -> None:
        print("After closing the browser")
    










