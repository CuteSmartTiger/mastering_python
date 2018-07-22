from functools import wraps

class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


# As an instance method
a = A()
@a.decorator1
def spam():
    pass


# As a class method
@A.decorator2
def grok():
    pass



# 这种方法在标准库中就有示例，比如说@property，实际是拥有
# getter()/setter()/deleter()方法的类，类中每一个定义的方
# 法可以作为装饰器
# 比如代码如下：
class Person:
    # Create a property instance
    first_name = property()

    # Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value