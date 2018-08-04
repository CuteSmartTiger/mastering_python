# 4.12chain()不同集合上元素的迭代
# 如果输入序列非常大的时候会很省内存。 并且当可迭
# 代对象类型不一样的时候 chain() 同样可以很好的工作。
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
c = ['x','y','z','u','v']
for x in chain(a, b):
    print(x,end=',')
# 1,2,3,4,x,y,z,
# 而for x in a + b:不推荐

# 返回的元组形式
for i in zip(a, b, c):
    print(i)
# (1, 10, 'x')
# (2, 11, 'y')
# (3, 12, 'z')

from itertools import zip_longest
for i in zip_longest(a, b, c,fillvalue =0):
    print(i)
# fillvalue为可选参数
# (1, 10, 'x')
# (2, 11, 'y')
# (3, 12, 'z')
# (0, 15, 'u')
# (0, 0, 'v')

print(zip(a, b))
# <zip object at 0x000001C6ABC97C88>

print(list(zip(a, b)))
[(1, 10), (2, 11), (3, 12)]
