


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



webdriverLocation = Service(executable_path="C:\\chromedriver.exe")

browser = webdriver.Chrome(service=webdriverLocation)

browser.get("https://www.google.com")

#login elements
loginButton = browser.find_element(By.ID, "login")
userNameButton = browser.find_element(By.ID, "username")
passwordButton = browser.find_element(By.ID,"password")

# action on login elements
userNameButton.send_keys("lokesh")
passwordButton.send_keys("lokeshreddy")
loginButton.click()


# clicking on the deposit link
browser.find_element(By.LINK_TEXT, "Deposit").click()

# clicking on the close FD/RD account link on the left navigation link
browser.find_element(By.LINK_TEXT,"Close FD/RD Account").click()


# select fixed deposit radio button
browser.find_element(By.ID, "Deposit Dropdown").click()

# Handling the dropdown using select class
dropDown = Select(browser.find_element(By.NAME, "Mydeposits"))
dropDown.select_by_value("1002")


# find the checkbox field
checkBox = browser.find_element(By.ID, "checkbox")
if (checkBox.is_selected()!= True):
    checkBox.click()

# or the following approach can be used.Uncomment the following to try.  
"""if(checkBox.get_attribute("checked")):
    checkBox.click()"""

# Select the transfer type
browser.find_element(By.ID,"Transfer Type").click()


# click on close deposit button
browser.find_element(By.ID,"closeDeposit").click()

# logout from the application
browser.find_element(By.ID, "Logout Button").click()

# close the browser
browser.close()

