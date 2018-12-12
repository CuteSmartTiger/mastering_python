#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 18:17
# @Author  : liuhu
# @Site    :
# @File    : thread_test.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import threading
import time

# 本案例主要解释线程的隔离，线程的名字是不同的，相互不影响的


def worker():
    print('hi')
    t = threading.current_thread()
    time.sleep(2)
    print(t.getName())


new_t = threading.Thread(target=worker, name='liuhu')
new_t.start()

t = threading.current_thread()
print(t.getName())
