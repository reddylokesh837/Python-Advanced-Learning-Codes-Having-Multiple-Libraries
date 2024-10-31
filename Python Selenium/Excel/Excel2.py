import xlrd
import xlwt
import xlutils
import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By

def readData(file_path):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    
    login_data =[]
    for row_idx in range(1,sheet.nrows):
        username = sheet.cell_value(row_idx,0)
        password = sheet.cell_value(row_idx,1)
        login_data.append([username,password])
    return login_data


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://demo.automationtesting.in/Datepicker.html")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def testLogin(self):
        login_data = readData("Packgo.xls")


        for data in login_data:
            login_link = self.driver.find_element(By.LINK_TEXT,"Login")

            login_link.click()

            username_field =self.driver.find_element(By.ID,"username").send_keys(data[0])
            password_field=self.driver.find_element(By.ID,"password").send_keys(data[1])


            login_button= self.driver.find_element(By.ID, "LoginButton")
            login_button.click()

            logout_link = self.driver.find_element(By.LINK_TEXT, "Logout")
            self.assertTrue(logout_link.is_displayed(),f"Login failed for {data[0]}")

            logout_link.click()