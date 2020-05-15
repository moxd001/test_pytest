from time import sleep

from test001.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element('link text','登录').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        sleep(2)
        self.driver.find_element('link text','立即注册').click()
        windows = self.driver.window_handles
        print(windows)
        self.driver.switch_to_window(windows[-1])
        sleep(2)