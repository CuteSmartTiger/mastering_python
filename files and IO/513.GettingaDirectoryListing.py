import os
# 获取该目录下的文件、目录、符号链接
names = os.listdir(r'C:\liuhu\note\documents')
print(names)


#  Get all regular files
names = [name for name in os.listdir(r'C:\liuhu\note\documents')
        if os.path.isfile(os.path.join(r'C:\liuhu\note\documents', name))]

# Get all dirs
dirnames = [name for name in os.listdir(r'C:\liuhu\note\documents')
            if os.path.isdir(os.path.join(r'C:\liuhu\note\documents', name))]


# 字符串的 startswith() 和 endswith() 方法对于过滤一个目录的内容也是很有用的
pyfiles = [name for name in os.listdir('somedir')
            if name.endswith('.py')]

import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
            if fnmatch(name, '*.py')]



# 获取元数据
# Example of getting a directory listing
import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, mtime)

# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)