# 14.8. Creating Custom Exceptions

# 创建新的异常很简单——定义新的类，让它继承自
# Exception （或者是任何一个已存在的异常类型）

class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class TimeoutError(NetworkError):
    pass

class ProtocolError(NetworkError):
    pass

try:
    msg = s.recv()
except TimeoutError as e:
    ...
except ProtocolError as e:


# 补充说明：
# 自定义异常类应该
# 总是继承自内置的
# Exception 类， 或
# 者是继承自那些本身
# 就是从 Exception 继
# 承而来的类。 尽管所有
# 类同时也继承自
# BaseException ，但
# 你不应该使用这个基
# 类来定义新的异常。 BaseException
# 是为系统退出异常而保留的，比如
# KeyboardInterrupt 或 SystemExit 以及
# 其他那些会给应用发送信号而退出的
# 异常。 因此，捕获这些异常本身没什么
# 意义。 这样的话，假如你继承 BaseException
# 可能会导致你的自定义异常不会被捕获而直接
# 发送信号退出程序运行。

# 2.想定义的新异常重写了 __init__() 方法，
# 确保你使用所有参数调用 Exception.__init__()
class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status


# 3.raise 函数中参数的个数，请注意
# Exception的默认行为是接受所有传递的参数并将它们以元组形式存储在 .args 属性中
# 注意看raise语句中使用的参数个数是怎样的：
try:
    raise RuntimeError('It failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)

('It failed', 42, 'spam')