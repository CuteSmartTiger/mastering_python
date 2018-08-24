# 9.14. Capturing Class Attribute Definition Order
from collections import OrderedDict

# A set of descriptors for various types
class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected ' + str(self._expected_type))
        instance.__dict__[self._name] = value

class Integer(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

# Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()

class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self,name)) for name in self._order)

# Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

# >>> s = Stock('GOOG',100,490.1)
# >>> s.name
# 'GOOG'
# >>> s.as_csv()
# 'GOOG,100,490.1'
# >>> t = Stock('AAPL','a lot', 610.23)
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "dupmethod.py", line 34, in __init__
# TypeError: shares expects <class 'int'>

# 2.防止重复的定义：
from collections import OrderedDict

class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super().__init__()
    def __setitem__(self, name, value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name, self.clsname))
        super().__setitem__(name, value)

class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return NoDupOrderedDict(clsname)

# >>> class A(metaclass=OrderedMeta):
# ... def spam(self):
# ... pass
# ... def spam(self):
# ... pass
# ...
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "<stdin>", line 4, in A
#     File "dupmethod2.py", line 25, in __setitem__
#         (name, self.clsname))
# TypeError: spam already defined in A
# >>>


# 3.ORM
# 在对象关系映射中，我们通常会看到下面这种方式定义的类：

class Stock(Model):
    name = String()
    shares = Integer()
    price = Float()