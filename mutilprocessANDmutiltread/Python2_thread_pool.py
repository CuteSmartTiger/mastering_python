#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 15:16
# @Author  : liuhu
# @File    : Python2_thread_pool.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import threading
from threadpool import *
import time
import random


# 定义线程函数
def do_func(task_id, data):
    global fail_list
    try:
        if task_id == 5 or task_id == 10:
            time.sleep(1)
            print data
            print "task_id:{0},failed".format(task_id)
            raise RuntimeError
        else:
            time.sleep(1)
            print "task_id:{0},succese".format(task_id)
            return True
    except RuntimeError:
        fail_list.append(task_id)


def handle_exception(request, exc_info):
    if not isinstance(exc_info, tuple):
        # 肯定有错误发生
        print(request)
        print(exc_info)
        raise SystemExit


mutil_args = [([5, 'ni hao'], None), ([8, 'hello'], None), ([3, 'hello'], None), ([10, 'hello'], None),
              ([4, 'hello'], None), ]
if __name__ == '__main__':
    pass
    # 创建线程池
    thread_pool = ThreadPool(20, poll_timeout=3)
    # 生产处理的任务清单
    requests = makeRequests(do_func, mutil_args)
    # 将任务放进线程池
    start_time = time.time()
    fail_list = []
    for req in requests:
        thread_pool.putRequest(req)
    thread_pool.wait()
    time_long = time.time() - start_time
    print fail_list
    print time_long
    # thread_pool.poll()
