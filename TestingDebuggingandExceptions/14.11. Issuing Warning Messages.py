# 14.11. Issuing Warning Messages

# 要输出一个警告消息，可使用 warning.warn() 函数

import warnings

def func(x, y, logfile=None, debug=False):
    if logfile is not None:
         warnings.warn('logfile argument deprecated', DeprecationWarning)

# warn() 的参数是一个警告消息和一个警告类，警告类有如下几种：
# UserWarning, DeprecationWarning, SyntaxWarning,
# RuntimeWarning, ResourceWarning, 或 FutureWarning.