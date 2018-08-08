import os
path = '/Users/beazley/Data/data.csv'
# Get the last component of the path
print(os.path.basename(path))
# data.csv

# Get the directory name
print(os.path.dirname(path))
# /Users/beazley/Data

# Join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))
# \的方向，与Linux系统下的相反
# tmp\data\data.csv

# Expand the user's home directory
path = '~/Data/data.csv'
print(os.path.expanduser(path))
# C:\Users\liuhu/Data/data.csv


# Split the file extension
print(os.path.splitext(path))
# ('~/Data/data', '.csv')



# 注意点：对于任何的文件名的操作，你都应该使用
# os.path 模块，而不是使用标准字符串操作来构造
# 自己的代码。 特别是为了可移植性考虑的时候更应
# 如此， 因为 os.path 模块知道Unix和Windows系统
# 之间的差异并且能够可靠地处理类似 Data/data.csv
# 和 Data\data.csv 这样的文件名