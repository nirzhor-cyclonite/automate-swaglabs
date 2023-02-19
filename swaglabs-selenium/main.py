# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import login
import VisitWebsite
import products
import cart
import checkout


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome("E:/ChromeDriver/chromedriver.exe", options = chrome_options)
    driver.maximize_window()


    expected_title = "Swag Labs"
    url_to_visit = "https://www.saucedemo.com/"
    first_name = "Rashedun"
    last_name = "Nobi"
    zip_code = 1216

    visitWebsite = VisitWebsite.StartUp(driver)
    visitWebsite.VISIT_WEBSITE(url_to_visit)
    visitWebsite.GET_WEBSITE_TITLE()

    login = login.Login(driver)
    login.LOGIN_SWAGLABS(expected_title)

    products = products.Products(driver)
    products.PURCHASE_PRODUCTS()

    time.sleep(2) #for presentation
    cart = cart.Cart(driver)
    cart.CLICK_BUTTON()

    checkout = checkout.Checkout(driver)
    checkout.SET_MY_INFORMATION(first_name, last_name, zip_code)
    checkout.CLICK_CONTINUE_BUTTON()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
