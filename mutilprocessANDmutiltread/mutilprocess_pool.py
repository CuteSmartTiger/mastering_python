#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import time

# 本节了解进程与进程池的用法
def spider(times):
    time.sleep(times)
    print('{0}子进程成功！！'.format(times))
    return "调用函数结果{0}".format(times)


if __name__ == '__main__':
    print('==============单进程测试=============')
    process = multiprocessing.Process(target=spider, args=(4,))
    print(process)
    process.start()
    print(process.pid)
    # 超过2秒，若子进程没有结束，则结束子进程
    process.join(timeout=2)
    print('主进程结束')

    print('========== 进程池测试 =============')
    # 进程池，可以获取每一个进程的结果
    print(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(spider,args=(3,))
    result1 = pool.apply_async(spider,args=(1,))
    # 等待所有子进程完成
    # 此处为什么要用close()
    pool.close()
    # 阻塞
    pool.join()
    print("result进程结果:{0}".format(result.get()))
    print("result1进程结果:{0}".format(result1.get()))

    print('============= 进程次中使用imap ========================')
    # imap执行多个子进程,阻塞式依次完成，与imap_unordered源码对比
    # 可知其内部实现机制为需要返回进程结果才可以返回值
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for result in pool.imap(spider,[1,4,2,3]):
        print('{0} sleep ended'.format(result))

    print('========= 进程次中使用imap_unordered ===========')
    # imap_unordered，非阻塞式
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for result in pool.imap_unordered(spider, [1, 4, 2, 3]):
        print('unorder {0} sleep ended'.format(result))