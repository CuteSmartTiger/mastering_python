# 9.18. Defining Classes Programmatically

# 目的：将类的定义源代码以字符串的形式发布出去。 并且使用函数比如 exec() 来执行它

#
# 可以使用函数 types.new_class() 来初始化新的类对象。
# 你需要做的只是提供类的名字、父类元组、关键字参数，
# 以及一个用成员变量填充类字典的回调函数

# stock.py
# Example of making a class manually from parts

# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price
def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__' : __init__,
    'cost' : cost,
}

# Make a class
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
# 对 Stock.__module__ 的赋值。， 每次当一个类被定义后，它的
# __module__ 属性包含定义它的模块名。 这个名字用于生成 __repr__() 方法的输出

# 2.想创建的类需要一个不同的元类，可以通过 types.new_class() 第三个参数传递
import abc
Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta},lambda ns: ns.update(cls_dict))

# 第三个参数还可以包含其他的关键字参数
class Spam(Base, debug=True, typecheck=False):
    pass
# 那么可以将其翻译成如下的 new_class() 调用形式：

Spam = types.new_class('Spam', (Base,),
                        {'debug': True, 'typecheck': False},
                        lambda ns: ns.update(cls_dict))