#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 23:52
# @Author  : liuhu
# @Site    : 
# @File    : map_or_dict.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Map:
    """ Map ADT list implemention
    Map()
    length()
    contains(key)
    add(key, value)
    remove(key)
    valudOf(key)
    iterator()
    """
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, 'Invalid map key'
        return self._entryList[ndx].value

    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, 'Invalid map key'
        self._entryList.pop(ndx)

    def __iter__(self):
        return _MapIterator(self._entryList)

    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None


class _MapEntry:    # or use collections.namedtuple('_MapEntry', 'key,value')
    def __init__(self, key, value):
        self.key = key
        self.value = value