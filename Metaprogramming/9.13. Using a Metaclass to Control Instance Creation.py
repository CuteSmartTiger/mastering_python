# 9.13. Using a Metaclass to Control Instance Creation

# 1.创建一个不可以实例化的类，只能用静态方法调用属性
# 思路：
# 1.定义一个元类并自己实现 __call__() 方法，方法中报错
class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

# 创建心类，然后继承元类
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

# 只可以调用这个类的静态方法，创建实例就会报错
Spam.grok(42)
Spam.grok
# s = Spam()
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
#     File "example1.py", line 7, in __call__
#         raise TypeError("Can't instantiate directly")
# TypeError: Can't instantiate directly

# 2.只能创建唯一实例的类（单例模式）
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

# a = Spam()
# Creating Spam
# b = Spam()
# >>>a is b
# True
# c = Spam()
# >>>a is c
# True


# 3.缓存实例
import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

# >>> a = Spam('Guido')
# Creating Spam('Guido')
# >>> b = Spam('Diana')
# Creating Spam('Diana')
# >>> c = Spam('Guido') # Cached
# >>> a is b
# False
# >>> a is c # Cached value returned
# True

# 4.实现单例模式的其他方法
class _Spam:
    def __init__(self):
        print('Creating Spam')

_spam_instance = None

def Spam():
    global _spam_instance

    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance