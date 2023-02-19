from selenium.webdriver.common.by import By
import VisitWebsite
import csv

class Products:
    def __init__(self, driver):
        self.driver = driver

    def GET_PRODUCT_WISHLIST(self, filename="product_list.csv"):
        with open(filename, 'r') as data:
            rows = csv.reader(data)
            product_dictionary: dict = {rows[0]: rows[1] for rows in rows}

        return product_dictionary

    def GENERATE_XPATH(self, product_name, search_for):
        if search_for== 'button':
            x_path = '//div[text() = "' + product_name + '"]/../../following-sibling::div/button'
        elif search_for == 'price':
            x_path = '//div[text() = "' + product_name + '"]/../../following-sibling::div/div'
        return x_path

    def ADD_PRODUCT_TO_CART(self, product_name = 'Sauce Labs Backpack'):
        x_path = self.GENERATE_XPATH(product_name, "button")
        try:
            element = self.driver.find_element(By.XPATH, x_path)
            element.click()
        except:
            print("Unable to locate element")

    def GET_PRODUCT_PRICE(self, product_name = 'Sauce Labs Backpack'):
        x_path = self.GENERATE_XPATH(product_name, "price")

        try:
            element = self.driver.find_element(By.XPATH, x_path)
            price_text = element.text
            price = float(price_text.lstrip('$'))
        except:
            print("Issues while getting price")

        return price

    def PURCHASE_PRODUCTS(self):
        total_bill = 0.0
        shopping_list = self.GET_PRODUCT_WISHLIST()
        for key, value in shopping_list.items():
            if(int(value) == 1):
                self.ADD_PRODUCT_TO_CART(key)
                total_bill += self.GET_PRODUCT_PRICE()

        print('Total Bill: ' + str(total_bill))
