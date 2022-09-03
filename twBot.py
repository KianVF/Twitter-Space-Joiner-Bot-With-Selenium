import selenium
from selenium import webdriver
# path to web driver
driverPath = r'C:\Users\program\Desktop\kPy\WebDriver\geckodriver.exe' 
# URL to open space
spaceUrl = 'https://twitter.com/i/spaces/1LyxBqMEMeEJN'
browser = webdriver.Firefox(
    executable_path=driverPath)
for _ in range(10):
    browser.get(spaceUrl)
    # finding the join button
    btn = browser.find_element_by_css_selector("div[role = 'button']")
    btn.click()
