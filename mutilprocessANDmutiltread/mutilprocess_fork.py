#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

# 本章节需要掌握的知识点：

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