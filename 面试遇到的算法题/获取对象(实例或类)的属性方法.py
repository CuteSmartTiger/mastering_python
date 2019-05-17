#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 17:15
# @Author  : liuhu
# @File    : 获取对象(实例或类)的属性方法.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Test(object):
    name = 'liu'

    def test(self):
        print 'test'

    @staticmethod
    def static(cls):
        print 'static'


print hasattr(Test, 'name')
print hasattr(Test, 'test')

print getattr(Test, 'name')
print getattr(Test, 'test')
print getattr(Test, 'static')

dic = {'name': 'liuhu'}
print dic.get('name')

print setattr(Test, 'age', 18)
print getattr(Test, 'age')


class Call(object):
    def __init__(self):
        self.contanier = dict()

    def __call__(self, *args, **kwargs):
        pass

    def add(self, key, value):
        self.contanier[key] = value

