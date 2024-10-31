import unittest
import xlrd
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class Exercise19_WriteExcel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure the appropriate driver is installed
        self.driver.maximize_window()
        self.driver.get("https://example.com")  # URL for the "Pack & Go" application
        self.driver.implicitly_wait(2)

    def testName(self):
        try:
            self.driver.find_element(By.LINK_TEXT,"login").click()
            self.driver.find_element(By.ID,"username").send_keys("lokesh")
            self.driver.find_element(By.ID,"password").send_keys("password")

            self.driver.find_element(By.ID,"login").click()

            self.driver.find_element(By.XPATH, "//[@id='sidemenu3']").click()
            self.driver.find_element(By.ID,"clearAccount").click()
            self.driver.find_element(By.LINK_TEXT,"Logout").click()
        except NoSuchElementException as ne:
            print(ne)

        except ElementNotInteractableException as ei:
            print(ei)
        
        except Exception as e:
            print(e)
        finally:
            self.driver.close()
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()