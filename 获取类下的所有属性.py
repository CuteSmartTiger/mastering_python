#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 15:10
# @Author  : liuhu
# @File    : 获取类下的所有属性.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Menu:
    stra = []

    def __init__(self):
        self.stra = self.methods()

    def updateProject(self, *args):
        print('updateProject')

    def restartProject(self, *args):
        print('restartProject')

    def restartTomcat(self, *args):
        print('restartTomcat')

    def stopTomcat(self, *args):
        print('stopTomcat')

    def startTomcat(self):
        print('startTomcat')

    def methods(self):
        print(dir(self))
        return (list(
            filter(lambda m: not m.startswith("__") and not m.endswith("methods") and callable(getattr(self, m)),
                   dir(self))))
        # return(list(filter(lambda m: not m.startswith("__") and not m.endswith("methods") , dir(self))))


if __name__ == '__main__':
    # print(Menu().methods())
    me=Menu()
    print(me.stra)
    for i in me.stra:
        getattr(me,i)()
