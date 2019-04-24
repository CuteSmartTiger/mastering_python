#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 15:29
# @Author  : liuhu
# @File    : 获取的当前时间的分秒级别.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# import time

# now_time=datetime.datetime.now()
# str_time=now_time.strftime("%Y-%m-%d %X")
# tup_time=time.strptime(str_time,"%Y-%m-%d %X")
# print(tup_time)
# time_sec=time.mktime(tup_time)
# time_sec+=1
# tup_time2=time.localtime(time_sec)
# str_time2=time.strftime("%Y-%m-%d %X",tup_time2)
# print(str_time)
# print(str_time2)
import datetime


def get_time_now():
    now_time = datetime.datetime.now()
    str_time = now_time.strftime("%Y-%m-%d %X")
    return str_time
