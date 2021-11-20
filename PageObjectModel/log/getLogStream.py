# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：将日志打印在控制台
    日期：2021/11/20 13:40
"""

import logging


def logStream():
    # 创建一个日志器
    logger = logging.getLogger()
    # 设置日志级别为info
    logger.setLevel(logging.INFO)
    # 日志想要输出到哪，就要制定输出目的地，控制台   要创建一个控制台处理器
    console = logging.StreamHandler()
    logger.addHandler(console)

    # 创建一个格式器
    # 设置日志格式
    fmt = '%(asctime)s %(filename)s %(levelname)s %(module)s %(funcName)s %(message)s'
    # 生成日志信息 生成时间  文件名   日志的状态  类名   方法名  日志内容
    fomator = logging.Formatter(fmt)
    # 优化及控制台格式
    console.setFormatter(fomator)

    # 创建一个处理器   文本处理器   制定日期信息输出到文本处理器
    filehandler = logging.FileHandler('../excute_logs/logger.log', encoding='utf-8')
    logger.addHandler(filehandler)

    # 设置logger.log文本格式
    filehandler.setFormatter(fomator)
    return logger
