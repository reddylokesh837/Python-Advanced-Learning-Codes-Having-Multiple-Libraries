
import xlwt
import xlutils
import unittest
import xlrd
from selenium import webdriver

from selenium.webdriver.common.by import By


class testApp(unittest.TestCase):
    url = "https://demo.automationtesting.in/Register.html"
    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(service="chromewebdriver")
        cls.browser.get(cls.url)
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(20)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    
    def testMethod(self):
        filePath = "Packgo.xls"
        WorkBook = xlrd.open_workbook(filePath)
        sheet = WorkBook.sheet_by_index(0)

        for i in range(1, sheet.nrows):
            order_type = sheet.cell_value(i,0)
            dish1 = sheet.cell_value(i,1)
            dish2= sheet.cell_value(i,2)

            self.browser.find_element(By.ID, "Order type").send_keys(order_type)
            self.browser.find_element(By.ID, "Main dish").send_keys(dish1)
            self.browser.find_element(By.ID, "Curry").send_keys(dish2)

            self.browser.find_element(By.ID, "Submit").click()

            alert = self.browser.switch_to.alert
            popup_message = alert.text
            alert.accept()

            print(f"Order: {order_type} {dish1} {dish2}")
            print(f"Popup Message: {popup_message}")

    


if __name__ == "__main__":
    unittest.main()

