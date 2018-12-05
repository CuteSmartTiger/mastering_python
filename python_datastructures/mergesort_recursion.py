#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 22:37
# @Author  : liuhu
# @Site    : 
# @File    : mergesort_recursion.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
from mastering_python.python_datastructures.mergesort import merge_sorted_list
def mergesort(theList):
    """ O(nlogn)，log层调用，每层n次操作
    mergesort: divided and conquer 分治
    1. 把原数组分解成越来越小的子数组
    2. 合并子数组来创建一个有序数组
    """
    print(theList)    # 我把关键步骤打出来了，你可以运行下看看整个过程
    if len(theList) <= 1:    # 递归出口
        return theList
    else:
        mid = len(theList) // 2

        # 递归分解左右两边数组
        left_half = mergesort(theList[:mid])
        right_half = mergesort(theList[mid:])

        # 合并两边的有序子数组
        newList = merge_sorted_list(left_half, right_half)
        return newList

tes = [4, 5, 6, 7, 8, 9,1, 2, 3, 4, 5, 6]
print(mergesort(tes))