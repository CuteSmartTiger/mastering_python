# 先看一个普通的类
class Son:
    pass
son = Son()
print(son)
# 创建出实例对象，位于<__main__.Son object at 0x000002168CA3FE80>
print('-------------2------------')
# 然后使用__new__方法对实例的创建进行拦截，检测实例如下：
class Son:
    def __new__(cls, *args, **kwargs):
        print('创建实例对象时被拦截 ')

son = Son()
print(son)             # 创建实例时被拦截

print('-------------3------------')
class Son:
    # def __new__(cls, *args, **kwargs):
    #     print('创建实例对象时被拦截 ')

    def __init__(self):
        print('实例初始化')
        self.name= 'liluhu'

    def __del__(self):
        print('对象被释放，生命周期结束')

son = Son()
#del son       #报错，内存中对象已经释放
print(son)
print(son.name)
# 实例初始化
# <__main__.Son object at 0x00000283E763FE10>
# liluhu
# 对象被释放，生命周期结束
