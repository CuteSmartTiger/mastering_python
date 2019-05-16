#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 11:57
# @Author  : liuhu
# @File    : 使用装饰器对函数进行性能测试.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(1000000)
