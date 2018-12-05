#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 19:43
# @Author  : liuhu
# @Site    : 
# @File    : 2.one_array.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import ctypes
import array


class Array:
    def __init__(self, size):
        assert size > 0, 'array size must be > 0'
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), 'out of range'
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), 'out of range'
        self._elements[index] = value

    def clear(self, value):
        """ 设置每个元素为value """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, items):
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._items):
            val = self._items[self._idx]
            self._idx += 1
            return val
        else:
            raise StopIteration


array_test = Array(10)
print(len(array_test))
array_test[0] = 2
array_test[9] = 3
print(array_test[0])
print(array_test[9])
print(array_test[4])
for i in array_test:
    print(i)
