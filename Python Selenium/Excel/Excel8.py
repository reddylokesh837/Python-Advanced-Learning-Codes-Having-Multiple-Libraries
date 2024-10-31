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
        self.browser.find_element(By.LINK_TEXT,"Order Now").click()
        table = self.browser.find_element(By.ID,"WeekendOffers")
        rows = table.find_elements(By.TAG_NAME,"tr")

        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("Weekend Offers")

        for i in range(1,len(rows)):
            cols= rows[i].find_elements(By.TAG_NAME,"td")
            for col in range(0,len(cols)):
                print(i)
                if (col==1):
                    sheet.write(i,0,cols[col].text)
                elif (col==2):
                    sheet.write(i,1,cols[col].text)
                else:
                    continue
        workbook.save("WeekendOffers.xls")

if __name__ =="__main__":
    unittest.main()