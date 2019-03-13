#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 10:13
# @Author  : liuhu
# @File    : 通过值获取键.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3

print Color(3)

print Color.red.value
print '----'
print type(Color(1))
print Color.__members__.items()

for name, member in Color.__members__.items():
    print member.name
    print member.value

