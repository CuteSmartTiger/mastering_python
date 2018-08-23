# 9.13. Using a Metaclass to Control Instance Creation

# 1.创建一个不可以实例化的类，只能用静态方法调用属性
# 思路：
# 1.定义一个元类并自己实现 __call__() 方法，方法中报错
class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

# Examp
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')