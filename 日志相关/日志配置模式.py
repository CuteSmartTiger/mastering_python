#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 15:51
# @Author  : liuhu
# @File    : 日志配置模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import logging
LOG_FORMAT = "[%(thread)s:%(asctime)s:%(msecs)d:%(levelname)s:%(filename)s:%(funcName)s:%(lineno)05d]: %(message)s"
logging.basicConfig(filename='vdimonitor.log', level=logging.DEBUG, format=LOG_FORMAT)
# logging.basicConfig(filename='vdimonitor.log', level=logging.ERROR, format=LOG_FORMAT)

# 在解释器运行时可以设置标准输出
# logging.basicConfig(stream=sys.stdout,level=logging.DEBUG, format=LOG_FORMAT)
