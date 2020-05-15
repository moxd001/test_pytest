import allure


@allure.link("http://www.baidu.com", name="百度一下")
def test_with_link():
    print("这是一条连接！！")
