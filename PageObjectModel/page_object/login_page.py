# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/18 22:35
    登录页面对象，实现登录
    登录流程
    关联元素：
    账号
    密码
    登录按钮

"""
from time import sleep

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    # URL
    url = "https://auth.huaweicloud.com/"
    # 页面元素
    user = (By.NAME, "userAccount")
    passwd = (By.XPATH, '//input[@class="hwid-input hwid-input-pwd"]')
    button = (By.XPATH, '//div[@class="hwid-btn hwid-btn-primary"]')

    # 元素的操作流程
    def login(self, username, password):
        # 访问URL,最大化
        self.open(self.url)
        # 输入账号
        sleep(5)
        self.input_(self.user, username)
        # 点击输入密码
        self.click(self.passwd)
        self.wait(6)
        self.click(self.user)
        # 输入密码
        self.input_(self.passwd, password)
        # 点击登录按钮
        self.click(self.button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = "13152027756"
    password = "gjs199074"
    # 实例化登录页
    lp = LoginPage(driver)
    lp.login(user, password)
