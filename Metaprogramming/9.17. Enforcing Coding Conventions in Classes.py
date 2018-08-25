# 9.17. Enforcing Coding Conventions in Classes

# 定义一个元类
# 一个基本元类通常是继承自 type 并重定义它的 __new__() 方法 或者是 __init__() 方法
class MyMeta(type):
    def __new__(self, clsname, bases, clsdict):
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super().__new__(cls, clsname, bases, clsdict)

class MyMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary

class Root(metaclass=MyMeta):
    pass

class A(Root):
    pass


class B(Root):
    pass

# 元类的一个关键特点是它允许你在定义的时候检查类的内容


#
# 2.作为更高级和实用的例子，下面有一个元类，它用来检测重载方法
# ，确保它的调用参数跟父类中原始方法有着相同的参数签名
from inspect import signature
import logging
class MatchSignaturesMeta(type):

    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # Get the previous definition (if any) and compare the signatures
            prev_dfn = getattr(sup,name,None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, prev_sig, val_sig)

# Example
class Root(metaclass=MatchSignaturesMeta):
    pass

class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass

# Class with redefined methods, but slightly different signatures
class B(A):
    def foo(self, a, b):
        pass

    def spam(self,x,z):
        pass

# WARNING:root:Signature mismatch in B.spam. (self, x, *, z) != (self, x, z)
# WARNING:root:Signature mismatch in B.foo. (self, x, y) != (self, a, b)


# 代码中有一行使用了 super(self, self) 并不是排版错误。 当使用元
# 类的时候，我们要时刻记住一点就是 self 实际上是一个类对象。 因此

# ，这条语句其实就是用来寻找位于继承体系中构建 self 父类的定义。