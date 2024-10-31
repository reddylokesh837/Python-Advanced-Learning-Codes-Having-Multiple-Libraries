import unittest
import xlrd
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException,ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException

import os

class Exercise19_WriteExcel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure the appropriate driver is installed
        self.driver.maximize_window()
        self.driver.get("https://example.com")  # URL for the "Pack & Go" application
        self.driver.implicitly_wait(2)

    def testWrite(self):
        try:
            if not os.path.exists("ps.xls"):
                raise FileNotFoundError("The file was not found!")
            
            workBook = xlrd.open_workbook("ps.xls")
            sheet = workBook.sheet_by_index(0)

            writebook = copy(workBook)
            writesheet = writebook.get_sheet(0)

            for row in range(1, sheet.nrows):
                try:
                    order_type = sheet.cell_value(row, 0)
                    dish1 = sheet.cell_value(row, 1)
                    dish2 = sheet.cell_value(row, 2)

                    self.driver.find_element(By.ID, "Order type").send_keys(order_type)
                    self.driver.find_element(By.ID, "Main dish").send_keys(dish1)
                    self.driver.find_element(By.ID, "Curry").send_keys(dish2)

                    self.driver.find_element(By.ID, "Submit").click()

                    alert = self.driver.switch_to.alert
                    popup_message = alert.text
                    alert.accept()

                    writesheet.write(row, 3, popup_message)
                    writesheet.write(row, 4, "pass")
                except NoSuchElementException:
                    writesheet.write(row,4, "Fail - Nosuchelement exception")
                    print(f"NoSuchElementException at row {row}. Element not found.")
                except StaleElementReferenceException:
                    writesheet.write(row,4, "Fail - StaleElementReferenceException")
                    print(f"StaleElementReferenceException at row {row}. Element not found.")
                except TimeoutException:
                    writesheet.write(row,4, "Fail - TimeoutException")
                    print(f"TimeoutException at row {row}. Element not found.")
                except ElementNotVisibleException:
                    writesheet.write(row,4, "Fail - ElementNotVisibleException")
                    print(f"ElementNotVisibleException at row {row}. Element not found.")
                except ElementNotInteractableException:
                    writesheet.write(row,4, "Fail - ElementNotInteractableException")
                except Exception as e:
                    writesheet.write(row,4,e)
                    print(f"Error at row {row}: {e}")
                
            writebook.save("prestupdated.xls")
        except FileNotFoundError as fnfe:
            print(fnfe)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()

    