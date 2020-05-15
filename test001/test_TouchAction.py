
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.touch_actions import TouchActions
def test_touch():
    options = Options()
    options.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(options=options)
    try:
        driver.get('https://www.baidu.com')
        driver.maximize_window()
        el = WebDriverWait(driver,10,0.5).until(lambda x:x.find_element(By.ID,'kw'))
        el.send_keys('selenium')
        el_btn = driver.find_element(By.ID,'su')
        action = TouchActions(driver)
        print(action)
        action.tap(el_btn).perform()
        sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

# class TestTouchAction:
#     def setup(self):
#         options=Options()
#         options.add_experimental_option('w3c',False)
#         self.driver = webdriver.Chrome()
#     def teardown(self):
#         self.driver.quit()
#     def test_touchaction_scrollbottom(self):
#         self.driver.get('https://www.baidu.com')
#         self.driver.maximize_window()
#         ele = WebDriverWait(self.driver,10,0.5).until(lambda x: x.find_element('id','kw'))
#         # ele = self.driver.find_element('id','kw')
#         ele.send_keys('selenium')
#         sleep(2)
#         ele1 = WebDriverWait(self.driver,10,0.5).until(lambda x: x.find_element('id','su'))
#         # ele1.click()
#         action = TouchActions(self.driver)
#         action.tap(ele1).perform()
#         action.scroll_from_element(ele1,0,10000).perform()
#         sleep(5)
# if __name__ == '__main__':
#     pytest.main()