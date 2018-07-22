# 把装饰器定义为类
# 定义中需要实现__call__(),__get__() 方法


import types
from functools import wraps
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

# 在类外使用装饰器
@Profiled
def add(x, y):
    return x + y

# 在类中使用装饰器
class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


print(add(2, 3))    #5
print(add(3, 3))    #6
print(add(4, 3))    #7
print(add.ncalls)   #3



s = Spam()
print(s.bar(1))         #<__main__.Spam object at 0x000001F39D74D4E0> 1
print(s.bar(2))         #<__main__.Spam object at 0x000001F39D74D4E0> 2
print(s.bar(3))         #<__main__.Spam object at 0x000001F39D74D4E0> 3
print(Spam.bar.ncalls)  #3
print(s.bar.ncalls)     #3



