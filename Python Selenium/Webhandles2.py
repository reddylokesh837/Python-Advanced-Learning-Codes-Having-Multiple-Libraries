
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common import by
import unittest





class PSRestaurantTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the WebDriver
        cls.browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        cls.browser.maximize_window()
        cls.browser.get("http://url_of_ps_restaurant") 

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    def testFetch(self):
        # wait for the order now link to be loaded
        order_now_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT,"Order Now"))
        )
        order_now_link.click()

        # wait for the weekend offers link to be loaded
        weekend_offers_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT,"Weekend Orders"))
        )
        weekend_offers_link.click() 


        # fetch the coupon codes
        weekend_coupon_code = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.XPATH,"//table[@id='weekend_offers']//td[@class='couponcode]"))
        )
        upcoming_coupon_code = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.XPATH,"//table[@id='upcoming_offers']//td[@class='couponcode]"))
        )

        print(f"Weekend offers coupon code: {weekend_coupon_code.text}")
        print(f"Upcoming offers coupon code: {upcoming_coupon_code.text}")

        # assertion not equal
        self.assertNotEqual(weekend_coupon_code.text,upcoming_coupon_code.text)



    
if __name__ == "__main__":
    unittest.main()





