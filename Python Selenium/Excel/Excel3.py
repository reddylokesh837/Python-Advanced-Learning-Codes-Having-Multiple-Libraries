import unittest
from selenium import webdriver
import xlrd
import xlwt
from selenium.webdriver.common.by import By

class TestApp(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(service="chromewebdriver")
        cls.browser.get("https://demo.automationtesting.in/Datepicker.html")
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def testLogin(self):
        Workbook = xlrd.open_workbook("Paclgo.xls")
        sheet = Workbook.sheet_by_index(0)

        for i in range(1,sheet.nrows):
            Username= sheet.cell_value(i,0)
            Password= sheet.cell_value(i,1)
            self.browser.find_element(By.LINK_TEXT,"LoginButton").click()
            self.browser.find_element(By.ID,"username").send_keys(Username)
            self.browser.find_element(By.ID,"password").send_keys(Password)

            self.browser.find_element(By.ID,"LoginButton").click()

            self.browser.find_element(By.LINK_TEXT,"Logout").click()





