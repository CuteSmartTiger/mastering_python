#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 0:12
# @Author  : liuhu
# @Site    : 
# @File    : 深入理解dict机制.py.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class ComprehensiveDict:
    name = 'liuhu'
    age= 25

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ('name',)

    def __getitem__(self, item):
        return getattr(self,item)

c = ComprehensiveDict()
print(dict(c))
print(dict())