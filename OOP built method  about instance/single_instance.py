# 装饰器的方法
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        print(cls)
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class MyClass(object):
    def __init__(self):
        self.age = 12

# MyClass = singleton(MyClass)

p1 = MyClass()
p1.age =11
p2 = MyClass()
print(p2.age)

# 使用基类
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)

# 元类
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Fo(object):
    __metaclass__ = Singleton

fo1 = Fo()
fo2 = Fo()

print(foo1 is foo2)
# Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过
# __metaclass__创建一个名字为Foo的类对象（我说的是类对象，请紧
# 跟我的思路）。如果Python没有找到__metaclass__，它会继续在Bar（
# 父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。如果
# Python在任何父类中都找不到__metaclass__，它就会在模块层次中去
# 寻找__metaclass__，并尝试做同样的操作。如果还是找不到__metaclass__
# ,Python就会用内置的type来创建这个类对象