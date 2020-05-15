from time import sleep

import pytest

from test001.base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element('id','kw').send_keys('selenium')
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        self.driver.find_element('xpath',"//*[@id='page']/a[10]").click()
        sleep(3)
        print(self.driver.execute_script("return document.title;return JSON.stringif(performance.timing)"))
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(2)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(5)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))