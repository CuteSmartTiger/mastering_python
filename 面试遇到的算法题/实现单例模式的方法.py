#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 17:00
# @Author  : liuhu
# @File    : 实现单例模式的方法.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# 通过类的__new__方法,用instance存储唯一的示例化对象：
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            # super参数代表从Singleton开始查找MRO下一个cls的属性或者方法
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


# 通过装饰器存储
p = Singleton()
g = Singleton()
print id(p)
print id(g)
