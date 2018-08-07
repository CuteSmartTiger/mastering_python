# 5.5. Writing to a File That Doesn’t Already Exist

# x只可以在python3以上可以用
with open('somefile', 'xt') as f:
    f.write('Hello\n')
# 如果文件是二进制的，使用 xb 来代替 xt


# 检测当前路径下的文件是否已经存在，若存在则写入
# import os
# if not os.path.exists('somefile'):
#     with open('somefile', 'wt') as f:
#         f.write('Hello\n')
# else:
#     print('File already exists!')