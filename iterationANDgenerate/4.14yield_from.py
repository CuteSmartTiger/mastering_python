# 4.14 展开嵌套的序列
# 掌握的知识点有：
# 1.ignore_types，isinstance
# 2.运行的机理

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x, end=',')


# 1,2,3,4,5,6,7,8,

# 若不用yield from 则
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x
