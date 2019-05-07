#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 23:35
# @Author  : liuhu
# @Site    : 
# @File    : bubble_sort.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def bubble_sort(target_list):
    '''bubble sort'''
    for i in range(len(target_list) - 1):
        flag = False  # 标记此趟比较是否发生交换
        for j in range(len(target_list) - i - 1):
            if target_list[j] > target_list[j + 1]:
                target_list[j], target_list[j + 1] = target_list[j + 1], target_list[i]
                flag = True

        # 优化：某一趟未发生交换时，跳出循环
        if not flag:
            # print('i== %d,break' % i)
            break
    return target_list


if __name__ == '__main__':
    target_list = [2, 3, 5, 19, 3, 5, 6, 7]
    print(bubble_sort(target_list))
