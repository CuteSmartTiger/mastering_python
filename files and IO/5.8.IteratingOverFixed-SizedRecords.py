# 5.8. Iterating Over Fixed-Sized Records

from functools import partial
RECORD_SIZE = 32
with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)

# functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象。
# 标记值 b'' 就是当到达文件结尾时的返回值

# Last, but not least, the solution shows the file being opened in binary mode. For reading
# fixed-sized records, this would probably be the most common case. For text files, reading
# line by line (the default iteration behavior) is more common.