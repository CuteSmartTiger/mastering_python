# 14.7. Catching All Exceptions

# 1.捕获所有异常除了（SystemExit, KeyboardInterrupt,
# and GeneratorEx）需要使用：Exception类
try:
...
except Exception as e:
...
    log('Reason:', e)
# 若果想捕获所有异常 change Exception to BaseException

# 2.将异常信息输出，举例子对比
def parse_int(s):
    try:
    n = int(v)
except Exception:
    print("Couldn't parse")

If you try this function, it behaves like this:
>>> parse_int('n/a')
Couldn't parse
>>> parse_int('42')
Couldn't parse

# 改进的方向是将异常实例存储到变量e上
# 如下：
def parse_int(s):
    try:
    n = int(v)
except Exception as e:
    print("Couldn't parse")
    print('Reason:', e)
# In this case, you get the following output, which indicates that a programming mistake
# has been made:
>>> parse_int('42')
Couldn't parse
Reason: global name 'v' is not defined