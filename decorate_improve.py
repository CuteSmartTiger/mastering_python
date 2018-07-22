# 文章2：
from functools import wraps
import logging

# 定义外层函数logged，使用return decorate返回装饰器函数
def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    # 定义一个装饰器，返回wrapper函数
    def decorate(func):
        # 对传入的参数进行相关操作
        logname = name if name else func.__module__
        print(logname)
        log = logging.getLogger(logname)
        print(log)
        logmsg = message if message else func.__name__
        print(logmsg)

        @wraps(func)
        # 定义wrapper函数，返回被装饰的func函数，即后面示例中的add函数或者spam函数
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate



@logged(logging.DEBUG)
def add(x, y):
    return x + y
print(add(2,5))

print("------")
@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

print(spam())