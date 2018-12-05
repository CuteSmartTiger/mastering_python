#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 20:17
# @Author  : liuhu
# @Site    :
# @File    : define_queue.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Queue:
    """ Queue ADT, use list。list实现，简单但是push和pop效率最差是O(n)
    Queue()
    isEmpty()
    length()
    enqueue(item)
    dequeue()
    """

    def __init__(self):
        self._qList = list()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._qList)

    def enqueue(self, item):
        self._qList.append(item)

    def dequeue(self):
        assert not self.isEmpty()
        return self._qList.pop(0)

duilie = Queue()
print(type(duilie))
print(dir(duilie))
duilie.enqueue(1)
duilie.enqueue('d')
duilie.enqueue({'key':'value'})
print(duilie.dequeue())
print(duilie.dequeue())
print(duilie.dequeue())