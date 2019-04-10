# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 10:51
# @Author  : liuhu
# @File    : 下载各种格式的文件.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


import requests
# url = 'http://192.168.6.33/downloads/18893ddf-dcb7-44a2-9dcb-880fc2cea203/VDIMonitor(64)-3.1.1.0409_SETUP.zip'
url = 'http://192.168.6.33/downloads/9d80bf0c-2500-4e31-8019-31c44e069d24/%E5%88%86%E5%B8%83%E5%BC%8F%E6%9C%8D%E5%8A%A1%E6%A1%86%E6%9E%B6%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E8%B7%B5.pdf'
res = requests.get(url)
playFile = open('liuhu.pdf', 'wb')
for chunk in res.iter_content(100000):
     playFile.write(chunk)

