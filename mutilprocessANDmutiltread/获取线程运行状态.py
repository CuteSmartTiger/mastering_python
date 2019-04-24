#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 13:45
# @Author  : liuhu
# @File    : 获取线程运行状态.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import threading
import time


def test1():
    j = 0
    while j < 100:
        j += 1
        print 'j== {0}'.format(j)
        time.sleep(1)
    return


def test2():
    j = 0
    while j < 100:
        j += 1
        print 'j== {0}'.format(j)
        print threading.enumerate()
        time.sleep(2)
        import datetime


import datetime


def get_time_now():
    now_time = datetime.datetime.now()
    str_time = now_time.strftime("%Y-%m-%d %X")
    return str_time


# def record_thread_status(*args):
#     '''获取线程的状态'''
#     # print list(args)
#     print args
#     while True:
#         for i in args:
#             if i.is_alive():
#                 print '{0} is alive'.format(i)
#             else:
#                 print '{0} is dead'.format(i)
#                 print args
#         time.sleep(1)

def record_thread_status(args):
    '''获取线程的状态'''
    # thread_list =  list(args)

    while True:
        # 当只有主线程时跳出循环，并记录日志
        thread_list = threading.enumerate()
        print thread_list
        if len(thread_list) == 1:
            with open('thread_status_main.txt', 'a+') as f:
                f.write("%s     MainThread is not alive \n" % get_time_now())
                break

        for i in args:
            print args
            print '移除之前'
            if not i.is_alive():
                args.remove(i)
                print '移除之后'
                print args

            with open('thread_status_%s.txt' % i.name, 'a+') as f:
                f.write("%s     Thread %s is alive or not :%s" % (get_time_now(), i.name, str(i.is_alive())) + '\n')
        time.sleep(1)




if __name__ == '__main__':
    t1 = threading.Thread(target=test1, name='test1')
    t2 = threading.Thread(target=test2, name='test2')
    t1.start()
    t2.start()
    # print t1.is_alive()
    # print t1.isAlive()
    # record_thread_status([t1, t2])
    # print threading.enumerate()
    time.sleep(3)
    print threading.enumerate()
