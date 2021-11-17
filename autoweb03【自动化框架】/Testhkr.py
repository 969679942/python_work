from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from InitPage import InitPage
from LoginOperation import LoginOpera
import time
from read_excel import get_data
from read_excel import wr_result
@ddt
class TestHkr(TestCase):
    # 在所有用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()




    @data(*get_data('HKR.xls','LOGIN'))
    @unpack
    def testLoginSuccess(self,a,b,c,d,e):

        username = a
        password = b
        expect = c


        login = LoginOpera(self.driver)

        # 执行登陆的三项惭怍
        login.login(username,password)


        # 获取实际结果
        result = login.getLoginSuccessResult()

        time.sleep(3)

        # 写入结果
        if result == expect:
            wr_result('HKR.xls', d, e, '通过', 0)
        else:
            wr_result('HKR.xls', d, e, '不通过', 0)
        # 断言
        self.assertEqual(expect,result)

    @data(*get_data('HKR.xls', 'LOGIN'))
    @unpack
    def testLoginError(self,a,b,c,d,e):

        username = a
        password = b
        expect = c


        login = LoginOpera(self.driver)

        # 执行登陆的三项惭怍
        login.login(username,password)


        # 获取实际结果
        result = login.getLoginErrorResult()

        time.sleep(3)

        # 写入结果
        if result == expect:
            wr_result('HKR.xls', d, e, '通过', 0)
        else:
            wr_result('HKR.xls', d, e, '不通过', 0)
        # 断言
        self.assertEqual(expect,result)





















