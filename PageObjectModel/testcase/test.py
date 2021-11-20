# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/18 23:28
"""
import unittest
from time import sleep

from selenium import webdriver
from page_object.login_page import LoginPage
from ddt import ddt, file_data
from reports.testReports import testReports

@ddt
class Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data("../data/user_data.yml")
    def test001(self, **kwargs):
        """
        function: login华为云
        description: 登录华为云
        arg:
        return:
        """
        self.lp.login(kwargs['user'], kwargs['password'])
        sleep(5)

    def test002(self):
        """
        function: 购买vpc
        description: 购买vpc
        arg:
        return:
        """
        print('the second testcase!')

    def test003(self):
        """
        function: 购买ecs
        description: 购买ecs
        arg:
        return:
        """
        print('the three testcase!')

    def test004(self):
        """
        function: 绑定服务器
        description: bind服务器
        arg:
        return:
        """
        print('the four testcase!')

    def test005(self):
        """
        function: 解绑服务器
        description:
        arg:
        return:
        """
        print('the five testcase!')

    def test006(self):
        """
        function: 删除vpc
        description:
        arg:
        return:
        """
        print('the six testcase!')

    def test007(self):
        """
        function: 删除ecs
        description:
        arg:
        return:
        """
        print('the seven testcase!')

    def test008(self):
        """
        function: 进入主页
        description:
        arg:
        return:
        """
        print('the eight testcase!')

    def test009(self):
        """
        function: 进入vpc界面
        description:
        arg:
        return:
        """
        print('the nigh testcase!')

    def test010(self):
        """
        function: 进入cdn界面
        description:
        arg:
        return:
        """
        print('the ten testcase!')


if __name__ == '__main__':
    testReports()
