#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 进程之间的通信，这里不可以使用queue中的Queue，必须使
# 用mutilprocessing中的Queue，进程之间无法使用全局变量进行通信
import time
from multiprocessing import Queue, Process, Manager, Pool


def producer(queue):
    id_num = 1
    while True:
        queue.put('{0}号面包'.format(id_num))
        print('生产了一个面包，编号为{0}'.format(id_num))
        id_num += 1
        time.sleep(2)


def consumer(queue):
    while True:
        time.sleep(2)
        data = queue.get()
        print('消费了{0}'.format(data))


if __name__ == '__main__':
    pool = Pool()
    # 使用Manager实例化的对象下的Queue实现进程池的通信
    queue = Manager().Queue(6)
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))
    pool.close()
    pool.join()
