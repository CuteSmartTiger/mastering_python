#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 0:10
# @Author  : liuhu
# @Site    : 
# @File    : stack_list.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
class Stack:
    """ Stack ADT, using a python list
    Stack()
    isEmpty()
    length()
    pop(): assert not empty
    peek(): assert not empty, return top of non-empty stack without removing it
    push(item)
    """
    def __init__(self):
        self._items = list()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)

    def peek(self):
        assert not self.isEmpty()
        return self._items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self._items.pop()

    def push(self, item):
        self._items.append(item)
