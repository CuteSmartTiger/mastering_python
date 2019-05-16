#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 15:19
# @Author  : liuhu
# @File    : 闭包的实验.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

def clousre(lis):
    dic = {}
    print 'dic'

    def test():
        for index, value in enumerate(lis):
            dic[index] = value
        return dic

    return test


print clousre([1, 2, 3])()
print clousre([4, 5, 6])()
