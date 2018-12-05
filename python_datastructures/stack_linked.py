#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 0:12
# @Author  : liuhu
# @Site    : 
# @File    : stack_linked.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Stack:
    """ Stack ADT, use linked list
    使用list实现很简单，但是如果涉及大量push操作，list的空间不够时复杂度退化到O(n)
    而linked list可以保证最坏情况下仍是O(1)
    """
    def __init__(self):
        self._top = None    # top节点, _StackNode or None
        self._size = 0    # int

    def isEmpty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def peek(self):
        assert not self.isEmpty()
        return self._top.item

    def pop(self):
        assert not self.isEmpty()
        node = self._top
        self.top = self._top.next
        self._size -= 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1


class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link


c= Stack()
c.push(1)
c.push(2)
c.push(3)
print(c.peek())
print(c.pop())
print(c.pop())
# print(c.peek())