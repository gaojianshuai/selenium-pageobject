# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/18 22:17
    作用：将常用的与项目适配的相关函数，进行二次封装，变成自定义函数，便于调用
    访问url、元素定位、输入、等待、点击、退出等等
    存在的意义：就是为了让页面对象进行继承，从而获得基本的方法，来实现页面的操作流程
"""
import time
from time import sleep
import logging
from selenium import webdriver
from log.base_logging import logger
from log.getLogStream import logStream

# # 设置日志格式
# fmt = '%(asctime)s %(filename)s %(levelname)s %(module)s %(funcName)s %(message)s'
# # 生成日志信息 生成时间  文件名   日志的状态  类名   方法名  日志内容
# # 设置日志级别      fomate日志格式     生成的日志文件保存在log.log文件里头
# logging.basicConfig(level=logging.DEBUG, format=fmt, filename='../excute_logs/log.log')

log = logStream()


# 创建基类
class BasePage:
    # driver = webdriver.Chrome()
    # 构造函数
    def __init__(self, driver):
        log.info('初始化driver{}'.format(driver))
        self.driver = driver

    # 访问URL
    def open(self, url):
        """
        function: 打开浏览器，访问url
        description:
        arg:
        return:
        """
        log.info('访问网址')
        self.driver.get(url)
        self.driver.maximize_window()

    # 元素定位
    def locator(self, loc):
        """
        function: 定位元素
        description:
        arg:
        return:
        """
        log.info('正在定位{}元素'.format(loc))
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):
        """
        function: 输入
        description:
        arg:
        return:
        """
        try:
            log.info('正在定位{}元素， 输入{}内容'.format(loc, txt))
            self.locator(loc).send_keys(txt)
        except Exception as e:
            self.screenShot()
            log.error('错误日志' % e)

    # 点击
    def click(self, loc):
        """
        function: 点击
        description:
        arg:
        return:
        """
        try:
            log.info('正在点击{}元素'.format(loc))
            self.locator(loc).click()
        except Exception as e:
            self.screenShot()
            log.error('错误日志' % e)

    # 等待
    def wait(self, time_):
        """
        function: 等待
        description:
        arg:
        return:
        """
        log.info('等待时间{}秒'.format(time_))
        sleep(time_)

    # 关闭
    def quit(self):
        """
        function: 退出
        description:
        arg:
        return:
        """
        log.info('退出')
        self.driver.quit()

    # 最大化
    def maxSize(self):
        """
        function: 最大化
        description:
        arg:
        return:
        """
        log.info('最大化')
        self.driver.maximize_window()

    # 截图并保存
    def screenShot(self):
        """
        function: 绑定服务器
        description: bind服务器
        arg:
        return:
        """
        current_time = time.strftime('%Y-%m-%d %H-%M-%S')
        print(current_time)
        pic_path = '../log/screenshot' + '/' + current_time + '.png'
        self.driver.save_screenshot(pic_path)

    # 关闭浏览器
    def close(self):
        """
        function: 关闭当前浏览器
        description:
        arg:
        return:
        """
        self.driver.close()

    # 刷新浏览器
    def refresh(self):
        """
        function: 刷新浏览器
        description:
        arg:
        return:
        """
        self.driver.refresh()
