#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 21:11
# @Author  : liuhu
# @Site    :
# @File    : recursion_test.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def print_rev(n):
    if n > 0:
        print(n)
        print_rev(n - 1)


print_rev(4)

print('-----------------')


def printInOrder(n):
    if n > 0:
        printInOrder(n - 1)
        print(n)


printInOrder(3)


# Recursive Binary Search
def recBinarySearch(target, theSeq, first, last):
    if first > last:    # 递归出口1
        return False
    else:
        mid = (first + last) // 2
        if theSeq[mid] == target:
            return True    # 递归出口2
        elif theSeq[mid] > target:
            return recBinarySearch(target, theSeq, first, mid - 1)
        else:
            return recBinarySearch(target, theSeq, mid + 1, last)

test = [i for i in range(1,20,2)]
print(test)
print(recBinarySearch(6, test, 0, 9))