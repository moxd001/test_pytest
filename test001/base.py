from selenium import webdriver
import os
class Base():
    def setup(self):
        #一行set browser=XXX
        #一行pytest XXX
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
