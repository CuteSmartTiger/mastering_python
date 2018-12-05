#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 22:30
# @Author  : liuhu
# @Site    : 
# @File    : mergesort.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

def merge_sorted_list(listA, listB):
    """ 归并两个有序数组，O(max(m, n)) ,m和n是数组长度"""
    print('merge left right list', listA, listB, end='')
    new_list = list()
    a = b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            new_list.append(listA[a])
            a += 1
        else:
            new_list.append(listB[b])
            b += 1

    while a < len(listA):
        new_list.append(listA[a])
        a += 1

    while b < len(listB):
        new_list.append(listB[b])
        b += 1

    print(' ->', new_list)
    return new_list


