import unittest
import xlrd
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.common.by import By

class Exercise19_WriteExcel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure the appropriate driver is installed
        self.driver.maximize_window()
        self.driver.get("https://example.com")  # URL for the "Pack & Go" application
        self.driver.implicitly_wait(2)

    def test_write_excel(self):
        workbook = xlrd.open_workbook("data.xls")
        sheet = workbook.sheet_by_value(0)

        writebook = copy(workbook)
        writesheet = writebook.get_sheet(0)


        for row in range(1, sheet.nrows):
            try:
                order_type = sheet.cell_value(row, 0)
                dish1 = sheet.cell_value(row, 1)
                dish2 = sheet.cell_value(row, 2)


                self.driver.find_element(By.ID,"Ordertype").send_keys(order_type)
                self.driver.find_element(By.ID,"Maindish").send_keys(dish1)
                self.driver.find_element(By.ID,"Curry").send_keys(dish2)

                self.driver.find_element(By.ID,"Submit").click()

                alert = self.driver.switch_to.alert
                popup_message = alert.text
                alert.accept()

                writesheet.write(row,3, popup_message)
                writesheet.write(row,4,"pass")
            except Exception as e:
                writesheet.write(row,4, "Fail")
                print(f"Error for row {row}: {e}")
        
        writebook.save("PSREST.xls")
        

if __name__ == "__main__":
    unittest.main()