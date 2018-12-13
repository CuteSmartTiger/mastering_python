#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 进程之间的通信，这里不可以使用queue中的Queue，
# 必须使用mutilprocessing中的Queue，进程之间无法使用全局变量进行通信
import time
from multiprocessing import Queue, Process, Manager, Pool, Pipe

# 本章节了解进程之间的通信

# shared作为共享内存块,类型为字典
def producer(shared):
    """
    :param shared: dict
    :return:
    """
    id_num = 1
    while True:
        # 向共享字典中添加数据
        shared[id_num] = '{0}号面包'.format(id_num)
        print('生产了一个{0}'.format(shared[id_num]))
        id_num += 1
        time.sleep(1)


def consumer(shared):
    """
    :param shared: dict
    :return:
    """
    while True:
        for key, value in shared.items():
            # 取出字典中的任务完成后删除
            print('消费了{0}'.format(shared.pop(key)))
            time.sleep(1)


if __name__ == '__main__':
    # pipe只能用于两个进程之间的通信，效率比较高，因为锁比较少
    shared_dict = Manager().dict()
    myproducer = Process(target=producer, args=(shared_dict,))
    myconsumer = Process(target=consumer, args=(shared_dict,))
    myproducer.start()
    myconsumer.start()
    myconsumer.join()
    myproducer.join()
    print('生产消费完毕')
