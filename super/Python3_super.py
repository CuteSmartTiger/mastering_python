#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 23:13
# @Author  : liuhu
# @Site    : 
# @File    : Python3_super.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 本章需要学习的知识点：
# 1. 构造函数时为什么需要调用super
# 2. super的执行顺序
class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        super().__init__()

if __name__ == '__main__':
    b= B()