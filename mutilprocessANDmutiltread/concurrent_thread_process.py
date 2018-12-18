#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 在操作系统中，进程相比线程切换时耗时更长
# 消耗CPU的，建议使用多进程
# 对I/O操作比较频繁的，建议使用多线程

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# 本节主要用来对比多线程与多进程

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# 模拟I/O操作
def opre_io(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    # 线程池与进程池实现了上线文管理的方法，推荐使用with方法
    # with ThreadPoolExecutor(3) as executor:
    #     all_tasks = [executor.submit(fib, n) for n in range(25, 40)]
    #     start_time = time.time()
    #     for future in as_completed(all_tasks):
    #         result = future.result()
    #         print(result)
    #     print('thread spend time:', time.time() - start_time)

    # # Windows系统下，如果进程不在main下执行则会报错
    with ProcessPoolExecutor(3) as executor:
        all_tasks = [executor.submit(fib, n) for n in range(25, 40)]
        start_time = time.time()
        for future in as_completed(all_tasks):
            result = future.result()
            print(result)
        print('process spend time:', time.time() - start_time)
    #
    # with ThreadPoolExecutor(40) as executor:
    #     all_tasks = [executor.submit(opre_io, n) for n in [1]*40]
    #     start_time = time.time()
    #     for future in as_completed(all_tasks):
    #         result = future.result()
    #         print(result)
    #     print('thread io spend time:', time.time() - start_time)

    # with ProcessPoolExecutor(3) as executor:
    #     all_tasks = [executor.submit(opre_io, n) for n in [1]*40]
    #     start_time = time.time()
    #     for future in as_completed(all_tasks):
    #         result = future.result()
    #         print(result)
    #     print('thread io spend time:', time.time() - start_time)