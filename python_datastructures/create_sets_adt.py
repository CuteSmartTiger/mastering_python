#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 20:42
# @Author  : liuhu
# @Site    : 
# @File    : create_sets_adt.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


#这个集合的设置暂时失败的
class Set:
    """ 使用list实现set
    Set()
    length()
    contains(element)
    add(element)
    remove(element)
    equals(element)
    isSubsetOf(setB)
    union(setB)
    intersect(setB)
    difference(setB)
    iterator()
    """
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __iter__(self):
        return self

    def __contains__(self, element):
        return element in self._theElements

    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    def remove(self, element):
        assert element in self, 'The element must be set'
        self._theElements.remove(element)

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet



set_test= set('1')
set_test= set({1,2,'int',(1,2,3)})
for i in set_test:
    print(i)
    print(type(i))
# 循环打印之前先自排序一下，整数 元组 字符串，不可以是可变对象

print(type({1}))
print(type(set([1,2,3])))

set_a_test = Set()
set_a_test.add([1,2,3])
print(set_a_test)


set_b_test = Set()
set_b_test.add([2,1,3])
print(set_b_test)

# if set_a_test == set_b_test:
#     print('equal')