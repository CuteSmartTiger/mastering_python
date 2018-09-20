# 多态

# 多态的概念
# 多态的简单应用

# 抽象类概念
# 抽象方法概念

import abc
# 定义抽象类或者抽象方法等抽象时，继承他的子类需要实现对应的方法，否则报错
class Animal(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractclassmethod
    def drink(cls):
        pass

class Dog(Animal):
    def eat(self):
        print('eat shit')

    @classmethod
    def drink(cls):
        print('drink water')
d = Dog()

def test(obj):
    obj.eat()

test(d)
d.drink()