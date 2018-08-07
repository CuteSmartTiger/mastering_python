# 将 print() 函数的输出重定向到一个文件中去

# 在 print() 函数中指定 file 关键字参数:

with open('test.txt', 'wt') as f:
    print('Hello World!', file=f)