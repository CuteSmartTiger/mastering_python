## python进阶之装饰器之定义一个可接受参数的装饰器、如何定义一个属性可由用户修改的装饰器、定义一个能接受可选参数的装饰器
### 2.1定义一个接受参数的装饰器
前言：在理解上一篇文章的基础上理解定义一个接受参数的装饰器
思路：在装饰器函数的外层再定义一个接受参数的函数，让他返回
装饰器函数，在装饰器函数中进行相关参数的进行操作
代码解析如下：
```
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

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

print(add(2,5))

输出：
__main__
<Logger __main__ (WARNING)>
add
7



@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

print(spam())
输出：
example
<Logger example (WARNING)>
spam
Spam!

None              #若def函数后面追加一个return “hello”,则最后一个None改为hello



小结：

@decorator(x, y, z)
def func(a, b):
    pass
装饰器处理过程跟下面的调用是等效的;

def func(a, b):
    pass
func = decorator(x, y, z)(func)

```
### 2.2 如何定义一个属性可由用户修改的装饰器

前言：定义一个可以传参数的装饰器，若现在需要给以动态修改装饰器的属性，改若何定义呢？

思路：此处使用访问器函数（accessor function），然后nonlocal 来修改内部变量，这里的属性是指装饰器上的属性

代码解析如下：
```
from functools import wraps, partial
import logging

# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
        return wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')



# level级别默认设置为DEBUG
logging.basicConfig(level=logging.DEBUG)
print(add(2, 3))
# DEBUG:__main__:add
# 5


# Change the log message
add.set_message('Add called')
print(add(2, 3))
# DEBUG:__main__:Add called
# 5


# Change the log level
add.set_level(logging.WARNING)
print(add(2, 3))
# WARNING:__main__:Add called
# 5


若使用其他对于属性直接访问的方法，只能访问到顶层装饰器，例如：
@timethis
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
        n -= 1
其中顶层装饰器函数为：@timethis，用直接访问属性的方法会失败，请记住这点

本小节的内容可以作为后续类装饰器的替代
 ```
### 2.3定义一个能接受可选参数的装饰器

可选参数的含义：即当有参数时，我们可以如此使用@decorate(*args，**kwargs)，当没有参数时，这样使用@decorate，需要跟之前的知识结合起来一起理解：

在代码示例与解析之前，我们来了解一下装饰器的调用，即理解装饰器是如何施加在函数上的，来看一下代码：
```
@logged
def add(x, y):
    return x + y

这个调用序列跟下面等价：

def add(x, y):
    return x + y

add = logged(add)

以上是装饰器不带参数的调用顺序，实际执行中add函数作为logged中的function进行调用，这个为不可接受参数的装饰器
作为对比，这里再看一下带参数的装饰器的调用，如下：

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')
调用序列跟下面等价：

def spam():
    print('Spam!')
spam = logged(level=logging.CRITICAL, name='example')(spam)
可以看到，首先传入的是装饰器的参数，而此时spam函数并未传入装饰器，这个为可接受参数的装饰器

要定义一个装饰器同时满足两个用法，这里需要用到partial,代码解析如下：
from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper

# Example use
@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')
```
如果觉得不够详细，或者没看懂，可以加微信invictus090，可免费咨询，希望大家一起前进
