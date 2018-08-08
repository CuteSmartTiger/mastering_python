# gzip compression
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

import zipfile
z = zipfile.ZipFile("test.zip", "r")
# 读取压缩文件中的文件名，可以多了解一下zipfile模块的类属性与方法
for filename in z.namelist():
        print(filename)
        bytes = z.read(filename)
        print(len(bytes))
# Python Cookbook 3rd Edition 2013.pdf
# 10280464
# swagger.pdf
# 1133747



# 所有的I/O操作都使用文本模式并执行Unicode的编码/解码。
# 类似的，如果你想操作二进制数据，使用 rb 或者 wb 文件模式


# gzip.open() 和 bz2.open() 接受跟内置的 open()
# 函数一样的参数， 包括 encoding，errors，newline
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

# gzip和bz2模块可以工作在许多类文件对象上，
# 比如套接字，管道和内存中文件等
import gzip
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
