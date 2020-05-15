import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class TestDemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_demo(self):

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        sleep(2)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)


if __name__ == '__main__':
    pytest.main()
