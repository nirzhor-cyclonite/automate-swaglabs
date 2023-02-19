from selenium.webdriver.common.by import By
import VisitWebsite


class Login:

    def __init__(self, driver):
        self.driver = driver

    def VERIFY_PAGE_TITLE(self, expected_title, observed_title):
        try:
            assert expected_title == observed_title
        except AssertionError:
            print("The titles do not match!")
        else:
            print("We have found a match here, my friend!")

    def GET_USERNAME_PASSWORD(self):

        #Using try-except such that null values are not returned

        try:
            element = self.driver.find_element(By.ID, "login_credentials")
            usernames_text = list(element.text.split("\n"))
            element = self.driver.find_element(By.CLASS_NAME, "login_password")
            password_text = list(element.text.split("\n"))

            username = usernames_text[1]
            password = password_text[1]
        except:
            print("An error occurred while fetching username and password")
            username = "default-user"
            password = "default-password"

        return  username, password

    def GET_ELEMENT(self, placeholder):
        try:
            xpath = '//input[@placeholder="'+placeholder+'"]'
            element = self.driver.find_element(By.XPATH, xpath)
        except:
            element = 'no-element'
        return element

    def SET_USERNAME_PASSWORD(self, username, password):
        try:
            element = self.GET_ELEMENT("Username")
            element.send_keys(username)
            element = self.GET_ELEMENT("Password")
            element.send_keys(password)
        except:
            print("Error occurred while entering credentials")

    def CLICK_SUBMIT_BUTTON(self):
        element = self.driver.find_element(By.ID, "login-button")
        element.click()

    def LOGIN_SWAGLABS(self, expected_title):
        expected_title = expected_title

        visitWebsite = VisitWebsite.StartUp(self.driver)
        observed_title = visitWebsite.GET_WEBSITE_TITLE()

        print("Title of the Page:", observed_title)
        self.VERIFY_PAGE_TITLE(expected_title, observed_title)

        username, password = self.GET_USERNAME_PASSWORD()
        print("Chosen Username: ",username,"\n", "Chosen Password: ", password, sep="")

        if(username != "default-user" and password != "default-user"):
            self.SET_USERNAME_PASSWORD(username, password)

            self.CLICK_SUBMIT_BUTTON()
            print("Submit button clicked")







