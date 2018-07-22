# 文章1
from functools import wraps
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """decorator"""
        print('Calling decorated function')
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

print(example.__name__, example.__doc__)
# 输出结果为：wrapper ，decorator


print('----------------')

# 使用@wraps，防止在使用装饰器时，函数运行后名称发生变化，示例已表明
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """decorator"""
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')
print(example.__name__, example.__doc__)


def fuck(func):
    print("fuck {!s}" .format(func.__name__[::-1].upper()))

@fuck
def wfg():
    pass
# wfg=fuck(wfg)



print('------------')

import time
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, func.__doc__,func.__annotations__,end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1
    return 'hello'

print(countdown(1000000))
print(countdown.__name__,countdown.__doc__,countdown.__annotations__)

print("--------------")


# 逆向获得函数信息
@timethis
def add(x,y):
    return x+y
or_add = add.__wrapped__
print(or_add(1,2))
print("----------")
print(add(1,2))


print("test")
from functools import wraps
def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

print(add(2, 3))
print('-----')
print(add.__wrapped__(2, 3))

