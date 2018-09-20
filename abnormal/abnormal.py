

# 1.自定义一个上下文管理器
def div(m,n):
    try:
        m/n
    # python2.x可以将as改为','，为了兼容所以统一使用as
    except ZeroDivisionError as e:
        print('不能除以0：',e)
    except NameError as x:
        print('---:',x)
    else:
        print('ji')
    finally:
        print(' wu di ')

# div(3,0)



# with 语句
# 需要了解的概念：上下文管理器  ___enter-__方法  ___exit__方法


# 自定义上下文管理器：
class test:
    def __enter__(self):
        print('start')

    # 参数对应实例，异常类型，异常值，异常追踪
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self, exc_type, exc_val, exc_tb)
        import traceback
        # 追踪信息正常打印，可以显示异常所在模块位置的详细信息与异常出现在模块的行位置
        print(traceback.extract_tb(exc_tb))
        print('end')
        # 若exit方法中返回True，则body体中出现异常会被内部消化，不会抛出异常
        # 若不返回值或者返回False,则依然会抛出异常
        return True

with test() as f:
    4/0

print('--将一个生成器改编为上下文管理器---')
# 2.将一个生成器改编为上下文管理器
# 上下文管理器的概念、把生成器变后哪部分是上文  哪部分是下文
import contextlib
@contextlib.contextmanager
def tes():
    try:
        print('hi')
        yield 'liuhu'
    except ZeroDivisionError as f:
        print('end:',f)

with tes():
    4/0


