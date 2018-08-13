# 14.13. Profiling and Timing Your Program

# 1.unix系统下，直接用time命令
time
python3
someprogram.py

# 2.查看更详细的报告，使用cProfile
python3 - m
cProfile
someprogram.py

# 3.对函数进行分析，使用装饰器
# timethis.py
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(10000000)
# __main__.countdown : 0.803001880645752

# 4.对语句块进行计时统计，定义上下文管理器
# 什么叫语句块
from contextlib import contextmanager


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))

with timeblock('counting'):
    n = 10000000
    while n > 0:
        n -= 1

# counting : 1.5551159381866455


# 5.针对短小的代码块做性能统计
from timeit import timeit
timeit('math.sqrt(2)', 'import math')
# 0.1432319980012835
timeit('sqrt(2)', 'from math import sqrt')
# 0.10836604500218527

# timeit 会执行第一个参数中语句100万次并计算
# 运行时间。 第二个参数是运行测试之前配置环境
# 。如果你想改变循环执行次数， 可以像下面这样
# 设置 number 参数的值：

timeit('math.sqrt(2)', 'import math', number=10000000)
# 1.434852126003534
timeit('sqrt(2)', 'from math import sqrt', number=10000000)
# 1.0270336690009572


# 6.对进程感兴趣：使用 time.process_time()
from functools import wraps
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper

# 如果你想进行更深入的性能分析，那么你需要详细阅读 time 、timeit 和其他相关模块的文档。