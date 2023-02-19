from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, driver):
        self.driver = driver

    def GET_BUTTON_XPATH(self, button_text):
        xpath = '//button[text() = "' + button_text + '"]'
        return  xpath

    def CLICK_BUTTON(self, button_text = 'Checkout'):
        x_path = self.GET_BUTTON_XPATH(button_text)
        element = self.driver.find_element(By.XPATH, x_path)
        element.click()