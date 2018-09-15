###调用操作
# __call__     实现实例的调用，在调用时可以传递参数
class Mom:
    # 为类实例初始化时赋值
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # def __call__(self, *args, **kwargs):   实现实例的可调用，同时可以在调用时对实例传参
    def __call__(self,child):
        print('{!s}的{!s},有一个孩子叫做{!s}'.format(self.age,self.name,child))

mom = Mom('nana',24)
mom('yaoyao')