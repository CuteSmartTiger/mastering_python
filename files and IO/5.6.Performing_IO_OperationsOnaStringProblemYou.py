import io
s=io.StringIO()
s.write('Hello World\n')

print('This is a test', file=s)

# Get all of the data written so far
print(s.getvalue())


# Wrap a file interface around an existing string
s = io.StringIO(r'Hello\nWorld\n')
print(s.read(4))
# Hell
print(s.read())
# o\nWorld\n


s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
# Hell
print(s.read())
# o
# World


# io.StringIO 只能用于文本。如果你要操作二进/
# 制数据，要使用 io.BytesIO 类来代替。

L = io.BytesIO()
L.write(b'binary data')
print(L.getvalue())
# b'binary data'


# 需要注意的是， StringIO 和 BytesIO 实例并没有正
# 确的整数类型的文件描述符。 因此，它们不能在那些
# 需要使用真实的系统级文件如文件，管道或者是套接字
# 的程序中使用。