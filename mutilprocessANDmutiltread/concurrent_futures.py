#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from concurrent import futures

# futures的submit  done result cancel方法
future = futures.Future()  # 未来对象：作为线程或者说task的返回容器


def spider(id, times):
    time.sleep(times)
    print('#{0}--->当前页面爬取成功！！'.format(id))
    return id, times


# 线程池初实例化对象时传递一个线程数量上限的参数
executor = futures.ThreadPoolExecutor(max_workers=2)

# submit()可以把待执行的函数提交到线程池，提交完后立即返回，返回值为一个实例化对象，可以看源码解析
task1 = executor.submit(spider, 1, 2)
task2 = executor.submit(spider, id=2, times=1)

# cancle()方法是把尚未运行的子线程从线程池中删除掉，这个还需在琢磨确认一下
task2.cancel()

time.sleep(1.5)
# done()方法为Future类提供的方法，用来判断任务是否完成
print(task1.done())
print(task2.done())

# result()方法为Future类提供的方法，用来获取执行结果，首先submit提交的函数需要有返回值，否则结果为None
print(task1.result())
print(task2.result())
