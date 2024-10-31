from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# Properly initialize ChromeDriver

driver = webdriver.Chrome()
# Navigate to Google
driver.get("https://www.google.com")

# Print the title and URL of the page
print(driver.title)
print(driver.current_url)

# Close the browser after test
# driver.quit()
