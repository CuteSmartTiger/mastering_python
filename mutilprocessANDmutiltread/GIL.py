#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GIL global interpreter lock 全局解释器锁 cpython
# Python中的一个线程对应C语言中的一个线程
# GIL使得同一个时刻只有一个线程在一个
# CPU上执行字节码，无法将多个线程映射
# 到多个CPU上执行
import dis

# GIL的概念

def test(a):
    a = a + 1
    return a


print(dis.dis(test))
# 输出
# 5           0 LOAD_FAST                0 (a)
#               2 LOAD_CONST               1 (1)
#               4 BINARY_ADD
#               6 STORE_FAST               0 (a)
#
#   6           8 LOAD_FAST                0 (a)
#              10 RETURN_VALUE
# None

# 全局解释器锁会在执行I/O操作或者执行固定长度的字节码或者CPU时间片到后释放
total = 0


def add(ran):
    """
    :param ran: int
    :return: int
    """
    global total
    for i in range(ran):
        total += 1
    print(total)
    return total


def sub(ran):
    """
    :param ran: int
    :return: int
    """
    global total
    for i in range(ran):
        total -= 1
    print(total)
    return total


# 在main一个主线程下开辟了两个子线程
if __name__ == "__main__":
    from threading import Thread

    # 此处还需理解daemon用法
    # add_thread = Thread(target=add, args=(1000000,), daemon=True)
    add_thread = Thread(target=add, args=(1000000,))
    # sub_thread = Thread(target=sub, args=(1000000,), daemon=True)
    sub_thread = Thread(target=sub, args=(1000000,))
    add_thread.start()
    sub_thread.start()
    # join表示通知主线程，对应的子线程结束后方可执行主线程
    add_thread.join()
    sub_thread.join()
