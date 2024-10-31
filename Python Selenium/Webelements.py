from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common import by

# selecting webdriver
webdriverLocation = Service(executable_path="C:\\chromedriver.exe")
# initiating instance
browser = webdriver.Chrome(service=webdriverLocation)


# launch the application
browser.get("https://www.google.com")

# maximizing the window and getting the browser title
browser.maximize_window()
print(browser.title)


# get the offers button
browser.find_element(By.LINK_TEXT, "Offers").click()

# get the table
table = browser.find_element(By.ID,"offersTable")

# get the rows
rows = table.find_element(By.TAG_NAME, "tr")
time.sleep(3)

print(len(rows))


# iterating through the list of rows
for row in range(0, len(rows)):
    print(rows[row].text)
    if(row!=0):
        # locating the columns the each row as in <td> tags within the <tr> tag
        cols = rows[row].find_elements(By.TAG_NAME,"td")
        for col in cols:
            print(col.text)


# closing the table
browser.find_element(By.ID,"crossTable").click()


# saving screenshot and closing the browser
browser.save_screenshot("pack.png")
browser.close()