# 需要掌握的知识点：__iter__的用法，生成器的用法

# 疑惑点：
# 1.思考如何自定义next方法，哪些对象可以使用next方法，next方法的实例用法深度解析
# 2.可接受迭代的内建函数有哪些，什么样的函数可以接受可迭代的函数，底层原理是
# 什么，知道这点，可以方便自己定义函数时，知道可以用哪些方法

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