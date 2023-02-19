class StartUp:

    def __init__(self, driver):
        self.driver = driver
    def VISIT_WEBSITE(self, my_url):
        self.driver.get(my_url)
    def GET_WEBSITE_TITLE(self):
        title = self.driver.title
        return title