# 14.6. Handling Multiple Exceptions

# 这一部分蛮有用的

# 1.一个单独的代码块，处理多个异常
try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)


# 2.针对某一个异常单独处理
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)


# 3.异常中的继承
try:
    f = open(filename)
except (FileNotFoundError, PermissionError):

try:
    f = open(filename)
except OSError:

# 其中FileNotFoundError, PermissionError是OSError的
# 子类，可以使用基类进行异常的捕获


# 4.使用as
try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error: %d', e.errno)
# 变量e获得OSError的实例


# 5.查看异常类之间的关系，可以得到类层次关系
# 使用__mro__属性
>>> FileNotFoundError.__mro__
(<class 'FileNotFoundError'>, <class 'OSError'>, <class 'Exception'>,
<class 'BaseException'>, <class 'object'>)


