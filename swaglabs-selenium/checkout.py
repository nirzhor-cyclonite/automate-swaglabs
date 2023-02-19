from selenium.webdriver.common.by import By
import cart

class Checkout:
    def __init__(self, driver):
        self.driver = driver

    def GET_ELEMENT(self, text_type, txt):
        try:
            xpath = '//input[@' + text_type + '="' + txt +'"]'
            element = self.driver.find_element(By.XPATH, xpath)
        except:
            element = 'no-element'
        return element

    def SET_MY_INFORMATION(self, first_name, last_name, zip_code):
        element = self.GET_ELEMENT("placeholder","First Name")
        element.send_keys(first_name)

        element.send_keys(last_name)
        element = self.GET_ELEMENT("placeholder","Last Name")
        element.send_keys(last_name)

        element = self.GET_ELEMENT("placeholder","Zip/Postal Code")
        element.send_keys(zip_code)

    def CLICK_CONTINUE_BUTTON(self):
        element = self.GET_ELEMENT("value", "Continue")
        element.click()
    def CLICK_CANCEL_BUTTON(self):

        temp_cart = cart.Cart(self.driver)
        temp_cart.CLICK_BUTTON("Cancel")
