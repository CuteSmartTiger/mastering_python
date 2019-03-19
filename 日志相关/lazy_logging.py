#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 19:52
# @Author  : liuhu
# @File    : lazy_logging.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
#coding=utf-8
import logging

logger = logging.getLogger('LazyLogging')
# logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
hander = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('[%(asctime)s: %(levelname)s in %(pathname)s:%(lineno)05d]: %(message)s ')
hander.setFormatter(formatter)
logger.addHandler(hander)

def getUserCount():
    logger.info('getUserCount is called')
    return 1

# logger.debug("There are " + str(getUserCount()) + " users logged in now.")
# logger.debug("There are %s users logged in now.", getUserCount())
logger.debug("There are %s users logged in now.", getUserCount())