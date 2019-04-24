#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 15:32
# @Author  : liuhu
# @File    : request__result.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import requests
import urllib
import json


requests_req = requests.get('http://cwzx.shdjt.com/cwcx.asp?gdmc=%CF%E3%B8%DB%D6%D0%D1%EB')
res = requests_req.text
print res
print requests_req.status_code


# ur = urllib.urlopen('http://192.168.6.95/v2/packages/')
# ur = urllib.urlopen('http://192.168.6.95/v2/packages?pagesize=5&pagenumber=1')
# ur = urllib.urlopen('http://192.168.6.95/v2/packages?pagesize=5&pagenumber=1')

# print json.loads(ur.read())
# print ur.info()
# print type(ur.read())
# print ur.getcode()








# r = requests.get('http://192.168.6.95/v2/packages')
# print r.json()
# print r.status_code
# print type(r.status_code)
