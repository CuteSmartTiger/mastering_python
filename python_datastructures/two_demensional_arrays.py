#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 20:27
# @Author  : liuhu
# @Site    : 
# @File    : 2.two_demensional_arrays.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
from one_array import Array
class TwoDemensionalArrays:
    """ 要实现的方法
    TwoDemensionalArrays(nrows, ncols):    constructor
    numRows()
    numCols()
    clear(value)
    getitem(i, j)
    setitem(i, j, val)
    """

    def __init__(self, numrows, numcols):
        self._the_rows = Array(numrows)  # 数组的数组
        for i in range(numrows):
            self._the_rows[i] = Array(numcols)

    @property
    def numRows(self):
        return len(self._the_rows)

    @property
    def NumCols(self):
        return len(self._the_rows[0])

    def clear(self, value):
        for row in self._the_rows:
            row.clear(value)

    def __getitem__(self, ndx_tuple):  # ndx_tuple: (x, y)
        assert len(ndx_tuple) == 2
        row, col = ndx_tuple[0], ndx_tuple[1]
        assert (row >= 0 and row < self.numRows and
                col >= 0 and col < self.NumCols)

        the_1d_array = self._the_rows[row]
        return the_1d_array[col]

    def __setitem__(self, ndx_tuple, value):
        assert len(ndx_tuple) == 2
        row, col = ndx_tuple[0], ndx_tuple[1]
        assert (row >= 0 and row < self.numRows and
                col >= 0 and col < self.NumCols)
        the_1d_array = self._the_rows[row]
        the_1d_array[col] = value
