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

    def tests(self):
        self.browser.find_element(By.LINK_TEXT, "Offers Link").click()
        table = self.browser.find_element(By.ID,"Offerstable")
        rows = table.find_elements(By.TAG_NAME,"tr")

        Workbook = xlwt.Workbook()
        sheets = Workbook.add_sheet("Offers List")
        for i in range(1,len(rows)):
            cols = rows[i].find_elements(By.TAG_NAME,"td")
            for j in range(len(cols)):
                print(i)
                if j == 1:
                    offers_details = cols[j].text
                    sheets.write(i,0,offers_details)
                elif j ==2:
                    coupons = cols[j].text
                    sheets.write(i,1,coupons)
                else:
                    continue
        Workbook.save("Loki.xls")


if __name__== "__main__":
    unittest.main()