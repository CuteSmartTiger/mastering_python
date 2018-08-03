# 需要掌握的知识点：__iter__的用法，生成器的用法

# 疑惑点：
# 1.思考如何自定义next方法，哪些对象可以使用next方法，next方法的实例用法深度解析
# 2.可接受迭代的内建函数有哪些，什么样的函数可以接受可迭代的函数，底层原理是
# 什么，知道这点，可以方便自己定义函数时，知道可以用哪些方法
# 3.itertools模块有哪些用法
# 优化点：

# 4.2 委托迭代
# 定义一个类，然后在类中定义方法
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

print(root._children)
# [Node(1), Node(2)]

# 4.3 使用生成器创建新的迭代模式
# 生成器的概念：
# 1.一个函数中需要有一个 yield 语句即可将其转换为一个生成器
# 2.生成器只能用于迭代操作
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 10, 2):
    print(n)


# 用for循环迭代它或者使用其他接受一个可迭代
# 对象的函数(比如 sum() , list() 等)
print(list(frange(0, 10, 2)))
print(sum(frange(0, 10, 2)))
# [0, 2, 4, 6, 8]
# 20



def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# 需要先实例化方可进行next方法，不可以多次使用print(next(countdown(4)))来
# 观察next()效果，否则得出的结果不会发生变化，实例化后m为一个可迭代对象，
# 暂时并没有运算出结果，每次使用next方法时，会依次迭代，而使用print(next
# (countdown(4)))，则每一次会从初始运行直接给出结果，而无法使用next方法
m=countdown(4)
print(next(m))
print(next(m))
print(next(m))
print(next(m))


# Starting to count from 4
# 4
# 3
# 2
# 1
# Done!


# 4.5反向迭代
# 类中定义了不同的方法，根据实际情况调用

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
# Countdown(5)调动__iter__方法，所以结果是从大到小打印
for rr in Countdown(5):
    print(rr,end="")
# 543211
print("\n")
# Countdown(5)调动__iter__方法,返回一个可迭代的对象，
# 然后调用__reversed__方法，从小到大打印
for rr in reversed(Countdown(5)):
    print(rr,end="")
# 12345


# 4.6 带有外部状态的生成器函数
# 思路：可以简单的将它实现为一个类，然后把生成器函数放到 __iter__() 方法中
from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        # def __init__(self, iterable, start=0)
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

print("\n")
# 打开文件查找含有python的行，输出行号与行的内容
with open('liuhu.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')




# 4.7迭代器切片
def count(n):
     while True:
        yield n
        n += 1

c = count(0)

# Now using islice()
import itertools
for x in itertools.islice(c, 10, 20):
     print(x)


# 4.8 跳过可迭代对象的开始部分
# 方法一：itertools.dropwhile() 函数，仅仅跳过开始部
# 分满足测试条件的行，在那以后，所有的元素不再进行测试和过滤了。
from itertools import dropwhile
with open('liuhu.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

print("\n")
# 方法二：islice()
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x,end=",")
# 1,4,10,15,
print("\n")
for x in islice(items,None,3):
    print(x,end=",")
# a,b,c,


# 方法三：会过滤掉所有以#号开头的行
with open('liuhu.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')


# 4.9 排列组合的迭代
# 情形一：每一个集合中的元素不可再元组中重复
items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)


# 情形二：元组中元素可以重复
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)

#  情形三：按参数个数进行组合
for p in permutations(items, 2):
    print(p)

# 情形四：无序组合
from itertools import combinations
for c in combinations(items, 2):
    print(c)

# 4.10 序列上索引值迭代
# enumerate() 函数
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 2):
    print(idx, val)
# 2 a
# 3 b
# 4 c

def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 5):
            print(lineno,line)
            fields = line.split()
            try:
                count = int(fields[1])
                print(fields)
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

parse_data("test.txt")

from collections import defaultdict
word_summary = defaultdict(list)

with open('test.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        # 字典赋值
        word_summary[word].append(idx)
print(word_summary)


# 4.11同时迭代多个对象
a = [1, 2, 3]
b = [10, 11, 12,15]
c = ['x','y','z','u','v']
for i,j in zip(a,b):
    print(i, j)
# 返回的是一对数值
# 1 10
# 2 11
# 3 12

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