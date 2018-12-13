#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 23:49
# @Author  : liuhu
# @Site    : 
# @File    : contextlib_test.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import contextlib


@contextlib.contextmanager
def customised_context(args):
    print('模仿enter方法')
    # 此处必须是一个生成器
    yield {}
    print('模仿exit方法')


with customised_context('args'):
    print('测试主体函数')

# 输出：
# 模仿enter方法
# 测试主体函数
# 模仿exit方法
