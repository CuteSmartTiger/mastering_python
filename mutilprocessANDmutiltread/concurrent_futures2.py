#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from concurrent import futures


# 穷举法比较低级，当需要已经成功完成的
# 任务的返回值时，应该使用as_completed()

def spider(id_num, times):
    time.sleep(times)
    print('#{0}--->当前页面爬取成功！！'.format(id_num))
    return id_num, times


def spiders(params):
    id_num = params.get('id_num')
    times = params.get('times')
    time.sleep(times)
    print('#{0}--->当前页面爬取成功！！'.format(id_num))
    return id_num, times


# 线程池初实例化对象时传递一个线程数量上限的参数
executor = futures.ThreadPoolExecutor(max_workers=2)

# as_completed本模块主要实现功为：获取已经
# 执行完毕的子线程，还可以获取子线程的返回结果
urls = [(1, 2), (2, 1), (3, 1.5), (4, 2.5)]
all_tasks = [executor.submit(spider, id_num, times) for id_num, times in urls]
# 可以详细了解as_completed的运行机理，可能迭代
# 时列表生成器中有部分已经执行完毕
for future in futures.as_completed(all_tasks):
    # result获取的是被调用函数return返回的结果，可以定制
    # 函数，获取多线程运行后的结果
    result = future.result()
    # 输出顺序由执行时间与列表生产式有关
    print('线程池中线程的执行结果：{0}'.format(result))

print('------------------')
urls = [(1, 2), (2, 1), (3, 1.5), (4, 2.5)]
all_tasks = [executor.submit(spider, id_num, times) for id_num, times in urls]
# 当有一个函数执行后主线程执行print方法，线程池里继续执行其他线程相关的任务
futures.wait(all_tasks, return_when=futures.FIRST_COMPLETED)
print('已经有一个线程执行完毕')8

print('------------------')
urls = [(1, 2), (2, 1), (3, 1.5), (4, 2.5)]
all_tasks = [executor.submit(spider, id_num, times) for id_num, times in urls]
# wait方法，等待所有线程完毕后才会继续执行print函数
futures.wait(all_tasks)
print('wait测试，已经有一个线程执行完毕')

print('------------------')
# 针对的executor通过map方法获取子线程的返回值
urlss = [{'id_num': 1, 'times': 2}, {'id_num': 2, 'times': 1}, {'id_num': 3, 'times': 1.5}, {'id_num': 4, 'times': 2.5}]
# map()函数直接返回result结果
for result in executor.map(spiders, urlss):
    # 输出顺序结果按照urlss中列表的顺序来的
    print(result)
