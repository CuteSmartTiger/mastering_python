#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 19:19
# @Author  : liuhu
# @Site    : 
# @File    : 1.ADT.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Bag:
    """
    constructor: 构造函数
    size
    contains
    append
    remove
    iter
    """
    def __init__(self):
        self._items = list()

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        assert item in self._items, 'item must in the bag'
        return self._items.remove(item)

    def __iter__(self):
        return _BagIterator(self._items)


class _BagIterator:
    """ 注意这里实现了迭代器类 """
    def __init__(self, seq):
        self._bag_items = seq
        self._cur_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_item < len(self._bag_items):
            item = self._bag_items[self._cur_item]
            self._cur_item += 1
            return item
        else:
            raise StopIteration


b = Bag()
b.add(1)
b.add(2)
print(b.__contains__(2))
print(b.remove(3))


for i in b:     # for使用__iter__构建，用__next__迭代
    print(i)


"""
# for 语句等价于
i = b.__iter__()
while True:
    try:
        item = i.__next__()
        print(item)
    except StopIteration:
        break
"""