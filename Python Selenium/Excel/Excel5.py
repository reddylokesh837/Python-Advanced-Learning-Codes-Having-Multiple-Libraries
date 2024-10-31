import select
import xlwt
import xlutils
import unittest
import xlrd
from selenium import webdriver

from selenium.webdriver.common.by import By

def readData(file_path):
    RestData = []

    book = xlrd.open_workbook("PS.xls")
    sheets = book.sheet_by_index(0)
    for i in range(1,sheets.nrows):
        Type = sheets.cell_value(i,0)
        Maindish = sheets.cell_value(i,1)
        Curry = sheets.cell_value(i,2)
        RestData.append([Type,Maindish,Curry])

    return RestData





class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://demo.automationtesting.in/Register.html")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def testLogin(self):
        order_link = self.driver.find_element(By.LINK_TEXT,"Order now").click()
        take_link = self.driver.find_element(By.LINK_TEXT,"Take away link").click()

        orders = readData("PS.xls")

        for order in orders:
            Type = order[0]
            Maindish = order[1]
            Curry = order[2]

            self.place_order(Type,Maindish,Curry)
    
    def place_order(self, order_type, dish1,dish2):
        print(f"Ordering {order_type} {dish1} and {dish2}")




if __name__=="__main__":
    unittest.main()