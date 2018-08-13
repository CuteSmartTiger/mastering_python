# 14.10. Reraising the Last Exception

# 1.单独使用raise
def example():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise

# 使用场景：
# 当你需要在捕获异常后执行某个操作
# （比如记录日志、清理等），但是之
# 后想将异常传播下去。 一个很常见的
# 用法是在捕获所有异常的处理器中
# 使用格式：

try:
    ....
except Exception as e:
# Process exception information in some way

# Propagate the exception
    raise