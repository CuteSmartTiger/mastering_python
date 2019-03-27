#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 11:37
# @Author  : liuhu
# @File    : 枚举测试.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


from enum import Enum


class PackageType(Enum):
    AGENT = 0
    TERMINAL = 1
    USERFILE = 2
    VDIMONITOR = 3
    SALTMINION = 4

print PackageType.TERMINAL.value