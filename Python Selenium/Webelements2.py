from curses.panel import bottom_panel
from faulthandler import is_enabled
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


# maximize the window and getting the browser title
browser.maximize_window()
print(browser.title)



browser.find_element(By.NAME,"login").click()
browser.find_element(By.ID,"usename").send_keys("lokesh")
browser.find_element(By.ID,"password").send_keys("password")
browser.find_element(By.ID,"login").click()


# select an option from source dropdown
sourceDropdown = Select(browser.find_element(By.ID, "sourceDropdown"))
sourceDropdown.select_by_visible_text("Bengaluru")

# select an option from destination dropdown
destDropdown = Select(browser.find_element(By.ID, "destinationDropdown"))
destDropdown.select_by_visible_text("Hyderabad")

# click searchbused option
browser.find_element(By.ID, "searchBuses").click()

# select a bus from a table
table = browser.find_element(By.ID, "busTable")
rows = table.find_element(By.TAG_NAME, "tr")

# based on time just select the preferred bus
for row in rows:
    columns = row.find_elements(By.TAG_NAME,"td")
    if "10:00 AM" in columns[2].text and "Available" in columns[4].text:
        row.find_elements(By.TAG_NAME, "button").click()
        break

# fill in the total number of tickets in the no of passengers field
passengerCount=3
if 1<= passengerCount<=5:
    browser.find_element(By.ID, "passengerField").send_keys(str(passengerCount))




# fill in the number of passengers
# passengers = BaseClass.browser.find_element(By.ID, "counter")
# passengers.clear()
# passengers.send_keys("2")

# click on calculate totla bill button
browser.find_element(By.ID, "calculateBillButton").click()

# check if the confirm button is enabled
confirmButton = browser.find_element(By.XPATH,"//button[@id='confirmbooking]")

if confirmButton.is_enabled():
    confirmButton.click()


# add a wait to handle the booking history
WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.ID,"bookingHistoryLink"))
).click()


# click on the refresh button
browser.find_element(By.ID,"refreshButton").click()

# display the booking details by iterating through the table

historyTable = browser.find_element(By.ID,"bookingHistoryTable")
historyRows = historyTable.find_element(By.TAG_NAME,"tr")

# iterating booking details

for row in historyRows:
    colums = row.find_elements(By.ID,"td")
    for column in columns:
        print("Booking details",column.text)


# logout of the application

browser.find_element(By.ID,"logoutLink").click()

browser.close()




browser.close()