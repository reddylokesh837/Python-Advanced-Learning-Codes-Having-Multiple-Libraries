import time
import xlwt
import xlutils
from xlutils.copy import copy
import unittest
import xlrd
from selenium import webdriver

from selenium.webdriver.common.by import By


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.browser = webdriver.Chrome(service="chromewebdriver")
        cls.browser.get("https://demo.automationtesting.in/Datepicker.html")
        cls.browser.maximize_window()
        cls.browser.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
    

    def testMethod(self):
        filePath = "Packgo.xls"
        WorkBook = xlrd.open_workbook(filePath)
        writeBook = copy(WorkBook)
        sheet = WorkBook.sheet_by_index(0)
        writesheet= writeBook.get_sheet(0)

        RowCount = sheet.nrows

        for i in range(1, RowCount):
            username = sheet.cell_value(i,1)
            password = sheet.cell_value(i,2)
            time.sleep(2)

            self.browser.find_element(By.LINK_TEXT,"Login").click()
            self.browser.find_element(By.ID,"username").send_keys(username)
            self.browser.find_element(By.ID,"password").send_keys(password)
            time.sleep(2)
            self.browser.find_element(By.ID,"LoginButton").click()

            if(self.browser.title=="Dashboard"):
                writesheet.write(i,3,"LoginSuccess")
                self.browser.find_element(By.ID,"Logout").click()
                if(sheet.cell_value(i,0)=="valid"):
                    writesheet.write(i,4,"Pass")
                else:
                    writesheet.write(i,4,"Fail")
            
            else:
                writesheet.write(i,3,"loginFailed")
                self.browser.find_element(By.ID,"closelogin").click()
                if(sheet.cell_value(i,0)=="invalid"):
                    writesheet.write(i,4,"Pass")
                else:
                    writesheet.write(i,4,"Fail")
        writeBook.save(filePath)




if __name__=="__main__":
    tc1 = unittest.TestLoader().loadTestsFromTestCase(TestApp)

    testsuite = unittest.TestSuite(tc1)
    unittest.TextTestRunner(verbosity=1).run(testsuite)