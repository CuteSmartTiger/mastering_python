#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 10:59
# @Author  : liuhu
# @File    : cmd_exe.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import subprocess
# cmd = [r'C:\vdiupdate\VDIMonitor-Setup.exe /S']
# cmd = [r'C:\vdiupdate\setup.bat']
# p = subprocess.Popen(cmd)
# p.communicate()

# 方法一：
import os
# main = r'C:\vdiupdate\VDIMonitor-Setup.exe /S'
main = r'C:\vdiupdate\VDIMonitor-Setup.exe  /S'
# r_v = os.system(main)
# 成功则返回值为0
# print (r_v )
url = 'http://192.168.6.33/downloads/5f0dc21b-b4bc-41fd-81a1-1415ac28f01e/VDIMonitor-3.1.1.0214-Setup.zip'
download_cmd = r'C:\vdiupdate\wget.exe {0}'.format(url)

# r_v = os.system(main)
# 成功则返回值为0
# print (r_v )


def download_package(package_url,filename):
    if os.path.exists(r'C:\vdiupdate\wget.exe'):
        download_cmd = r'C:\vdiupdate\wget.exe "{0}"  -P "C:\vdiupdate"'.format(package_url)
        return_code= os.system(download_cmd)
        if return_code ==0:
            if os.path.exists(r'C:\vdiupdate\{0}'.format(filename)):
                return True
            return False
        return False

def upzip_package(packagename,filename):
    if os.path.exists(r'C:\vdiupdate\unzip.exe'):
        cmd = r'C:\vdiupdate\unzip.exe -o "C:\vdiupdate\{0}" -d "C:\vdiupdate"'.format(packagename)
        return_code= os.system(cmd)
        if return_code ==0:
            if os.path.exists(r'C:\vdiupdate\{0}'.format(filename)):
                os.remove(r'C:\vdiupdate\{0}'.format(packagename))
                return True
            return False
        return False

re = download_package(url,r'VDIMonitor-3.1.1.0214-Setup.zip')
if re:
    upzip_package('VDIMonitor-3.1.1.0214-Setup.zip','VDIMonitor-Setup.exe')
# 方法二：
# import os
# main = "project1.exe"
# f = os.popen(main)
# data = f.readlines()
# f.close()
# 安装成功，但是返回内容为空
# print (data)