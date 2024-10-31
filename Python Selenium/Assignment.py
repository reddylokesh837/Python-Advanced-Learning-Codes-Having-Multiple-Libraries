"""Test Steps:

Launch the browser & open the "Pack & go" application.
Click on login link.
Log in to the application.
Select an option from source dropdown.
Select an option from destination dropdown.
Search for buses.
Select a bus slot.
Print the current URL of the browser.
Close the browser.


"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select




webdriverLocation = Service(executable_path="C:\\chromedriver.exe")

browser = webdriver.Chrome(service=webdriverLocation)


# go to the bus booking website
browser.get("https://www.google.com")

# find and select the login
browser.find_element(By.LINK_TEXT, "Login").click()



# find and enter your login details and then click on login
browser.find_element(By.ID, "usernameLogin").send_keys("Lokesh")
browser.find_element(By.ID, "userPassword").send_keys("lokeshreddy")
browser.find_element(By.ID, "login").click()


# after logging in we have to select the source and destination locations
# we can find the source dropdown element in this way
# browser.find_element(By.XPATH, "//select[@id='formDD']/option[1]")
browser.find_element(By.XPATH, "//select[@id='fromDD']")
browser.find_element(By.XPATH, "//option[@value='Bengaluru']").click()


# In short, Select is the better and preferred option when interacting with dropdown menus in Selenium.
# or we can select using Select class
from selenium.webdriver.support.ui import Select

#Locate the source dropdown
source_dropdown = browser.find_element(By.ID,"formDD")

# Select is a webdriver class which provides the implementation of the HTML SELECT Tag
# A SELECT Tag provides helper methods to select and deselect options.
# Create an instance of the select class by passing on the drop-down element as an argument.
# you cannot combine the creation of the Select object and the call to the select_by_value() method in a single line like that. The Select object needs to be initialized first, and then you can call methods on it.
select_source = Select(source_dropdown)


# previous statement defines an element instance
# selecting an option can be done in three ways
# select_by_index
# select_by_value
# select_by_visible_text

select_source.select_by_value("Bengaluru")





# for destination element:
# find dropdown first
dest_dropdown = browser.find_element(By.ID, "toDD")
# select dropdown using Select
select_dest = Select(dest_dropdown)
# select by value/index/visible_text
select_dest.select_by_value("Hyderabad")

# find and click the searchbus after setting the source and destination locations
browser.find_element(By.ID, "SearchBus").click()




# after we will get the buses list, we have to select the correct bus from the row list
# we can select the 3rd radio positioned bus and clicked on the radio
browser.find_element(By.XPATH, "//*[@id='radio3']").click()


browser.find_element(By.ID, "book").click()


print(browser.current_url)



# for deselecting:
source_dropdown = browser.find_element(By.ID, "fromDD")

select_source = Select(source_dropdown)
select_source.deselect_by_value("Bengaluru")


# for already selected option

sourceDropdown = browser.find_element(By.ID, "fromDD")
selectSource = Select(sourceDropdown)
selectSource.select_by_value("Bengaluru")

# first selected option returns a webelement instance
# first_selected_option: This function returns the first selected or the currently selected option in the select tag. It returns an instance of WebElement.
currentSelection = selectSource.first_selected_option

print(currentSelection.text)


# options: Returns a list of all options that belong to a particular select tag. It collects the option tag elements in a list of type WebElement.Refer the below code snippet to understand the usage of this function.
options = selectSource.options
print(len(options))

# for printing option's text one by one
for option in options:
    print(option.text)



# is_multiple: This function is used to check whether the SELECT element supports multiple options to be selected at the same time or not
multipleOptions = selectSource.is_multiple
print(multipleOptions)

# all_selected_options: Returns a list of all selected options that belong to a select tag
selectedList = selectSource.all_selected_options
print(len(selectedList))


for selected in selectedList:
    print(selected.text)



# select the bus slot row
radioButton = browser.find_element(By.XPATH,"//some-path")
# to check the selection state of a radio button
#  using is_selected(): A function that checks whether the button is selected, if selected, it returns true else it returns false.
if (radioButton.is_selected()!= False): 
    radioButton.click()


# we have another diff methods:
# select the bus slot row
#  get_attribute("checked"): This is a familiar method; we will discuss how this can be used in checking the selection state.
radioButton = browser.find_element(By.XPATH,"some-path")
# to check the selection state of a radio button
if (radioButton.get_attribute("checked")):
    radioButton.click()




# we can do same for the checkboxes also:
# select the checkbox field
checkBox = browser.find_element(By.ID, "idnumber")

# to check the selection state of a checkbox
if (checkBox.is_selected()!= False):
    checkBox.click()


# we can use attribute method also:
checkBox = browser.find_element(By.ID, "idnumber")
if (checkBox.get_attribute("checked")!= False):
    checkBox.click()







