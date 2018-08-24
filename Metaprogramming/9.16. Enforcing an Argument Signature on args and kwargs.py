# 9.16. Enforcing an Argument Signature on *args and**kwargs

# 作用：通过将签名和传递的参数绑定起来，可以强制函数调用遵循特
# 定的规则，比如必填、默认、重复等

# 从inspect模块导入两个类
from inspect import Signature, Parameter
# Make a signature for a func(x, y=42, *, z=None)
# 定义parms
parms = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
            Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
            Parameter('z', Parameter.KEYWORD_ONLY, default=None) ]
# 获得签名对象
sig = Signature(parms)
# print(sig)
# (x, y=42, *, z=None)
# 使用它的 bind() 方法将它绑定到 *args 和 **kwargs

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
         print(name,value)


# 2.强制函数签名更具体的例子
from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
            for name in names]
    return Signature(parms)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

# Example use
class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')

class Point(Structure):
    __signature__ = make_sig('x', 'y')

# import inspect
# >>> print(inspect.signature(Stock))
# (name, shares, price)
# >>> s1 = Stock('ACME', 100, 490.1)
# >>> s2 = Stock('ACME', 100)
# Traceback (most recent call last):
# ...
# TypeError: 'price' parameter lacking default value
# >>> s3 = Stock('ACME', 100, 490.1, shares=50)
# Traceback (most recent call last):
# ...
# TypeError: multiple values for argument 'shares'
# >>>


# 3.自定义元类来创建签名对象
from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
            for name in names]
    return Signature(parms)

class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields',[]))
        return super().__new__(cls, clsname, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

# Example
class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

# 当我们自定义签名的时候，将签名存储在特定的属性 __signature__
# 中通常是很有用的。 这样的话，在使用 inspect 模块执行内省的代
# 码就能发现签名并将它作为调用约定


# >>> import inspect
# >>> print(inspect.signature(Stock))
# (name, shares, price)
# >>> print(inspect.signature(Point))
# (x, y)