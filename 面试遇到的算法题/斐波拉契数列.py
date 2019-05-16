#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 12:58
# @Author  : liuhu
# @File    : 斐波拉契数列.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def fb1(n):
    """输出第n斐波拉契数值"""
    assert n > 0, 'n must > 0'
    a, b = 1, 0
    cout = 1
    while cout < n:
        a, b = a + b, a
        cout += 1
    return a


print fb1(9)


# print fb1(-1)


# 输出小于n的最后一个斐波拉契数
def last_one_fb(n):
    assert n > 1, 'n must > 1'
    a, b = 1, 0
    while a < n:
        a, b = a + b, a
    return b


print last_one_fb(35)


# 输出斐波拉契数列
def fb_list(n):
    assert n > 0, 'n must > 0'
    a, b = 1, 0
    lis = []
    cout = 0
    while cout < n:
        a, b = a + b, a
        cout += 1
        lis.append(b)
    return lis


print fb_list(4)
