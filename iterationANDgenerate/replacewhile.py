import sys

# stdout用法

f = open('liuhu.txt')
# iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一
# 个标记(结尾)值作为输入参数。 当以这种方式使用的时候，它会创建
# 一个迭代器， 这个迭代器会不断调用 callable 对象直到返回值和标
# 记值相等为止。
for chunk in iter(lambda: f.read(10), ""):
    n = sys.stdout.write(chunk)

print('\n',n)
# 1

