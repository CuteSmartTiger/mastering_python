#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 14:57
# @Author  : liuhu
# @File    : 获取页面信息.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import  requests
url= 'http://192.168.6.43/admin/assignments/virtualmachines_manage_page'
res = requests.get(url)
print res.content
print res.text