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
        print 'new'
        if not cls.__instance:
            # super参数代表从Singleton开始查找MRO下一个cls的属性或者方法
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __call__(self, *args, **kwargs):
        print 'call'


p = Singleton()
g = Singleton()
print id(p)
print id(g)

import functools


# 通过装饰器缓存存储用来实例对象的类
def singleton(cls):
    _instance = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper


@singleton
class Person(object):
    pass


t1 = Person()
t2 = Person()
print id(t1)
print id(t2)


# 元类实现单例的原理是控制类的创建，不存在则创建并存储
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(object):
    __metaclass__ = Singleton


o = MyClass()
o1 = MyClass()
print id(o)
print id(o1)
