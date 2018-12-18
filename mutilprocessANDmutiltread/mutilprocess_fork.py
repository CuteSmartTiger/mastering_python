#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

# 本章节需要掌握的知识点：
# 1.fork创建子进程，将父进程的所有数据复制到自
# 己的进程进行执行，进程之间的数据是隔离的，所以
# 进程之间无法像线程之间使用全局变量进行通信

# 理解fork在Linux中的使用方法后，可以方便后续
# 理解进程之间通信的方法，与线程间批次通信的区别

# fork 只用于Linux或Unix系统中，会返回两次
# 子进程或复制父进程
print('here')
pid = os.fork()
# print('here')
print(pid)
if pid ==0:
    print('子进程id是{0}，父进程id是{1}'.format(os.getpid(),os.getpid()))
else:
    print('我是父进程id：{0}'.format(pid))

import time
# 可以在Linux实验，此处如果取消主进
# 程的休息，则子进程会在主进程结束后
# 另起一个界面打印
time.sleep(3)