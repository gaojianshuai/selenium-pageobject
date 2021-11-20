# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/20 12:22
    debug:调试   1级
    info:系统正常运行    2级
    warning:警告信息
    error:错误，出现 问题
    critical:严重  快要崩溃
    常用info和error
"""

import logging


def logger():
    # 设置日志格式
    fmt = '%(asctime)s %(filename)s %(levelname)s %(module)s %(funcName)s %(message)s'
    # 生成日志信息 生成时间  文件名   日志的状态  类名   方法名  日志内容
    # 设置日志级别
    logging.basicConfig(level=logging.INFO, format=fmt, filename='../excute_logs/log.log')
    return logging

# 想要生成的日志信息   调用   日志级别
# logging.debug('debug日志模式')
# logging.info('info正常模式')
# logging.warning('warning警告模式')
# logging.error('error模式')
# logging.critical('critical严重的模式')
