# 13.9. Finding Files by Name
import os

# # os.walk()函数的使用，其返回三元组
#
# # start 指开始查找的起始目录，name指找到的目标文件，将
# # 匹配的绝对路径打印出来
# def findfile(start, name):
#     # relpath是指正在检视的目录的路径
#     # dirs指的是检视目录下的目录列表
#     # 该检视目录中所有文件的列表
#     for relpath, dirs, files in os.walk(start):
#         print(relpath)
#         print(dirs)
#         print(files)
#         if name in files:
#             full_path = os.path.join(start, relpath, name)
#             print(os.path.normpath(os.path.abspath(full_path)))
#
# if __name__ == '__main__':
#     # findfile(sys.argv[1], sys.argv[2])
#     findfile(r'C:\liuhu\note\documents\mastering python\Utility Scripting and System Administration','test.txt')

# C:\liuhu\note\documents\mastering python\files and IO\test.txt
# C:\liuhu\note\documents\mastering python\iterationANDgenerate\test.txt
# C:\liuhu\note\documents\mastering python\Utility Scripting and System Administration\test.txt


# 查找最近N天的修改过的文件
import os
import time
def modified_within(top, seconds):
    now = time.time()
    print(now)
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)

if __name__ == '__main__':
   import sys
# if len(sys.argv) != 3:
# print('Usage: {} dir seconds'.format(sys.argv[0]))
#     raise SystemExit(1)

modified_within(r'C:\liuhu\note\documents\mastering python', str(360))