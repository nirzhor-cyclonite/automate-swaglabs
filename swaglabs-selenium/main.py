# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import login
import VisitWebsite


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome("E:/ChromeDriver/chromedriver.exe", options = chrome_options)
    driver.maximize_window()


    expected_title = "Swag Labs"
    url_to_visit = "https://www.saucedemo.com/"

    visitWebsite = VisitWebsite.StartUp(driver)
    visitWebsite.VISIT_WEBSITE(url_to_visit)
    visitWebsite.GET_WEBSITE_TITLE()

    login = login.Login(driver)
    login.LOGIN_SWAGLABS(expected_title)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
