# pip install selenium

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# Store the keyword in a variable
keyword = input("Enter What Do You Need To Search in Google: ")

# Open the Chrome Browser
browser = webdriver.Chrome(executable_path=r"C:\Users\MRP\Downloads\chromedriver_win32\chromedriver.exe")

# Load Google Homepage
browser.get('https://www.google.co.in/')

# Find and Clear the search bar
searchbar = browser.find_element_by_name("q")
searchbar.clear()

# Paste the keyword and click enter
searchbar.send_keys(keyword)
searchbar.send_keys(Keys.RETURN)

print("Program Finished Successfully...")
