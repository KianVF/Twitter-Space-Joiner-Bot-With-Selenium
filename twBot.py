import selenium
from selenium import webdriver
driverPath = input(
    "Enter valid geckodriver.exe path example: C:\\Users\\program\\Desktop\\kPy\\WebDriver\\geckodriver.exe: ")
spaceUrl = input(
    "Enter a valid active twitter space URl Example : https://twitter.com/i/spaces/1LyxBqMEMeEJN: ")
n = int(input("Enter how many times you wish to connect to the space: "))
browser = webdriver.Firefox(executable_path=driverPath)
for _ in range(n):
    try:
        browser.get(spaceUrl)
        btn = browser.find_element_by_css_selector("div[role = 'button']")
        btn.click()
    except:
        print("Error occurred")
