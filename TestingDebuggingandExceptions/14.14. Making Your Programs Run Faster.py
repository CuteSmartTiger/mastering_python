# 14.14. Making Your Programs Run Faster


# 1.将全局范围运行的代码定义到函数中，
# 原理：局部变量的操作要比全局变量要快
# 原代码：
import sys
import csv
with open(sys.argv[1]) as f:
    for row in csv.reader(f):

# 改进后：
import sys
import csv
def main(filename):
    with open(filename) as f:
        for row in csv.reader(f):
# Some kind of processing
main(sys.argv[1])


# 2.有选择的消除属性访问
# 原理：每一次使用点(.)操作符来
# 访问属性的时候会带来额外的开销。
# 它会触发特定的方法，比如 __getattribute__()
# 和 __getattr__() ，这些方法会进行字典操作操作
# 使用场景：只有在大量重复代码中才有意义，比如循环
# 原代码：
import math
def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result
# Test
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)

# 改进后：
from math import sqrt
def compute_roots(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result



# 3.进一步优化：理解变量所处的位置
# 应用场景：局部变量会比全局变量运行速度快。 对于频繁访问的名称，
# 通过将这些名称变成局部变量可以加速程序运行
import math
def compute_roots(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result

# 4.避免不必要的抽象
# 对于类中的属性访问也同样适
# 用于这个原理。 通常来讲，查找某个
# 值比如 self.name 会比访问一个局部变量
# 要慢一些。 在内部循环中，可以将某个需
# 要频繁访问的属性放入到一个局部变量
# Slower
class SomeClass:
    ...
    def method(self):
        for x in s:
            op(self.value)

# Faster
class SomeClass:
    ...
    def method(self):
        value = self.value
         for x in s:
            op(value)

# 5.不必要的装饰器
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
        def y(self):
        return self._y
    @y.setter
        def y(self, value):
        self._y = value
# Now, try a simple timing test:
>>> from timeit import timeit
>>> a = A(1,2)
>>> timeit('a.x', 'from __main__ import a')
0.07817923510447145
>>> timeit('a.y', 'from __main__ import a')
0.35766440676525235

# 6.使用内建的容器


# 7.避免创建不必要的数据结构或复制