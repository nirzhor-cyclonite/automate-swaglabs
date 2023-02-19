from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Milestone_3_4:
    def __init__(self, my_url):
        self.my_url = my_url
        # keep browser window open
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(chrome_options = chrome_options)
        self.driver.maximize_window()

    def GET_WEBSITE_TITLE(self):
        self.driver.get(self.my_url)
        title = self.driver.title
        return title

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

    def VISIT_WEBSITE(self, expected_title):
        expected_title = expected_title
        observed_title = self.GET_WEBSITE_TITLE()

        print("Title of the Page:", observed_title)
        self.VERIFY_PAGE_TITLE(expected_title, observed_title)

        username, password = self.GET_USERNAME_PASSWORD()
        print("Chosen Username: ",username,"\n", "Chosen Password: ", password, sep="")

        if(username != "default-user" and password != "default-user"):
            self.SET_USERNAME_PASSWORD(username, password)

            self.CLICK_SUBMIT_BUTTON()
            print("Submit button clicked")







