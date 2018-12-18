#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# futures包
from concurrent import futures

# 深刻理解futures包中的Future对象
from concurrent.futures import Future

# 与semaphore相比
#1. futures包让线程池与进程池的接口一致，
# 方便编码，有利益后续学习协程
# 2.主线程中可以获取某一个线程的状态或者
# 某一个任务的状态以及返回值
# 3. 当一个线程完成的时候我们的主线程和多进程编码接口一致


# futures的submit  done result cancel方法
# 1.done方法时非阻塞的
# 2. result方法时阻塞的
# 3. submit提交后立即执行，返回一个Future对象


# 未来对象：作为线程或者说task的返回容器
future = futures.Future()


def spider(id, times):
    time.sleep(times)
    print('#{0}--->当前页面爬取成功！！'.format(id))
    return id, times


# 线程池初实例化对象时传递一个线程数量上限的参数
executor = futures.ThreadPoolExecutor(max_workers=2)

# submit()可以把待执行的函数提交到线程池，提交完后立即
# 返回，返回值为一个实例化对象，可以看源码解析，非阻塞
task1 = executor.submit(spider, 1, 2)
task2 = executor.submit(spider, id=2, times=1)

# cancle()方法是把尚未运行的子线程从线程池中删除
# 掉，这个还需在琢磨确认一下
task2.cancel()

time.sleep(1.5)
# done()方法为Future类提供的方法，用来判断
# 任务是否完成，非阻塞式
print('task1完成情况:{}'.format(task1.done()))
print('task2完成情况:{}'.format(task2.done()))

time.sleep(1)
print('--------------------====睡眠一会后========-------------')
print('task1完成情况:{}'.format(task1.done()))
print('task2完成情况:{}'.format(task2.done()))
print('--------------------==============-------------')

# result()方法为Future类提供的方法，阻塞式，用来获取执行结果，
# 首先submit提交的函数需要有返回值，否则结果为None
print(task1.result())
print(task2.result())
