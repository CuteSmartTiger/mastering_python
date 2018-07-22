# 装饰器为被包装函数增加参数
from functools import wraps

def optional_debug(func):
    @wraps(func)
    #此方法不可以随意为被包装函数增加参数，需要使用关键字的方法进行
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def spam(a,b,c):
    print(a,b,c)
    return "hello"

print(spam(1,2,3))
# 1 2 3
# hello

print(spam(1,2,3, debug=True))
# Calling spam
# 1 2 3
# hello

# 使用场所：对于重复的代码可以进行优化