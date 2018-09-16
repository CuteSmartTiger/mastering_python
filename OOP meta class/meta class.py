# type 为最底层的元类
type(3)
print(str.__class__)

# 通过type定义类
def sun():
    print('light')
class Base:
    @classmethod
    def base(cls):
        print('base')
meta_class = type('liuhu',(Base,),{'sun':sun})



print(meta_class.sun())
print(meta_class.base())
print(meta_class.__dict__)

# 元类查找机制：
# 按如下顺序依次查找：
# __metaclass__
# 继承的父类
# 当前模块是否有定义__metaclass__
# 查找type





