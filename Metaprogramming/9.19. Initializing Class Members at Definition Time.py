# 9.19. Initializing Class Members at Definition Time

# 目的：在类被定义的时候就初始化一部分类的成员，而不是要等到实例被创建后

import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)

class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

class Point(StructTuple):
    _fields = ['x', 'y']

s = Stock('ACME', 50, 91.1)
print(s)

print(s[0])
# 'ACME'
print(s.name)
# 'ACME'
print(s.shares * s.price)
# 4555.0