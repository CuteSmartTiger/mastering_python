#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 23:42
# @Author  : liuhu
# @Site    : 
# @File    : quicksort.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
def quicksort(theSeq, first, last):    # average: O(nlog(n))
    """
    quicksort :也是分而治之，但是和归并排序不同的是，采用选定主元（pivot）而不是从中间
    进行数组划分
    1. 第一步选定pivot用来划分数组，pivot左边元素都比它小，右边元素都大于等于它
    2. 对划分的左右两边数组递归，直到递归出口（数组元素数目小于2）
    3. 对pivot和左右划分的数组合并成一个有序数组
    """
    if first < last:
        pos = partitionSeq(theSeq, first, last)
        # 对划分的子数组递归操作
        quicksort(theSeq, first, pos - 1)
        quicksort(theSeq, pos + 1, last)


def partitionSeq(theSeq, first, last):
    """ 快排中的划分操作，把比pivot小的挪到左边，比pivot大的挪到右边"""
    pivot = theSeq[first]
    print('before partitionSeq', theSeq)

    left = first + 1
    right = last

    while True:
        # 找到第一个比pivot大的
        while left <= right and theSeq[left] < pivot:
            left += 1

        # 从右边开始找到比pivot小的
        while right >= left and theSeq[right] >= pivot:
            right -= 1

        if right < left:
            break
        else:
            theSeq[left], theSeq[right] = theSeq[right], theSeq[left]

    # 把pivot放到合适的位置
    theSeq[first], theSeq[right] = theSeq[right], theSeq[first]

    print('after partitionSeq {}: {}\t'.format(theSeq, pivot))
    return right    # 返回pivot的位置


def test_partitionSeq():
    l = [0,1,2,3,4]
    assert partitionSeq(l, 0, len(l)-1) == 0
    l = [4,3,2,1,0]
    assert partitionSeq(l, 0, len(l)-1) == 4
    l = [2,3,0,1,4]
    assert partitionSeq(l, 0, len(l)-1) == 2

test_partitionSeq()


def test_quicksort():
    def _is_sorted(seq):
        for i in range(len(seq)-1):
            if seq[i] > seq[i+1]:
                return False
        return True

    from random import randint
    for i in range(100):
        _len = randint(1, 100)
        to_sort = []
        for i in range(_len):
            to_sort.append(randint(0, 100))
        quicksort(to_sort, 0, len(to_sort)-1)    # 注意这里用了原地排序，直接更改了数组
        print(to_sort)
        assert _is_sorted(to_sort)

test_quicksort()


# 利用快排中的partitionSeq操作，我们还
# 能实现另一个算法，nth_element，快速查
# 找一个无序数组中的第k大元素
def nth_element(seq, beg, end, k):
    if beg == end:
        return seq[beg]
    pivot_index = partitionSeq(seq, beg, end)
    if pivot_index == k:
        return seq[k]
    elif pivot_index > k:
        return nth_element(seq, beg, pivot_index-1, k)
    else:
        return nth_element(seq, pivot_index+1, end, k)

def test_nth_element():
    from random import shuffle
    n = 10
    l = list(range(n))
    shuffle(l)
    print(l)
    for i in range(len(l)):
        assert nth_element(l, 0, len(l)-1, i) == i

test_nth_element()