# 第一步：自定义错误类型，需要继承于Exception
# 第二步：调用函数，出现异常情况是手动抛出异常给外界
# 第三部：外界使用try 方法，捕获异常

# 此方法的主要目的是编写模块给外界用时，出现传值错误时
# 需要向模块外报错，而不是继续运行

class GrowError(Exception):
    def __init__(self,msg,code):
        self.msg = msg
        self.code = code

    def __str__(self):
        return self.msg + str(self.code)

def set_age(age):
    if age <18:
        raise GrowError('未成年',401)
    else:
        print('成年')
try:
    set_age(17)
except GrowError as f:
    print(f)