# 方法一：
def check(func):
    def inner():
        print('check password')
        func()
    return inner

@check
def log():
    print('loging')

log()


print('-------------------方法2-----------')

def check(func):
    def inner():
        print('check password')
        func()
    return inner


def log():
    print('loging')

log = check(log)
log()

print('---------------使用类实现装饰器-----------')
class check:
    # 初始化时保存传入的函数
    def __init__(self,func):
        self.fan = func

    # 定义call方法方可调用实例
    def __call__(self, *args, **kwargs):
        print('check password')
        # 调用时执行函数
        self.fan()

def log():
    print('loging')

# 通过check类创建实例对象
log = check(log)
# 加上()，调用call方法
log()