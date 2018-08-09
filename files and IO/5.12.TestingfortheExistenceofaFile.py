# 1.检测文件或者目录是否存在
# 2.判断是文件 是目录
# 3.判断是不是软连接
# 4.判断是不是真实的地址
# 使用 os.path 模块来测试一个文件或目录是否存在

# 判断：输出的是布尔值

import os
# linux系统下判断是文件或者目录，两者之一，不确定哪一种，
# Windows可以直接根据输入的信息进行判断
print(os.path.exists('test'))

# Is a regular file
print(os.path.isfile('test.txt'))


# Is a directory
print(os.path.isdir('test'))


# Is a symbolic link
print(os.path.islink('/usr/local/bin/python3'))


# Get the file linked to
print(os.path.realpath('/usr/local/bin/python3'))
# '/usr/local/bin/python3.3'

# 获取文件大小
print(os.path.getsize('test.txt'))
# 获取目录修改时间
print(os.path.getmtime('test'))

import time
print(time.ctime(os.path.getmtime('test')))
