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