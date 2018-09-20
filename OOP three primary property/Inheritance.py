# 继承
# 一个类‘拥有’另一个类的‘资源’方式之一
# 拥有：资源的使用权，而不是复制，这点要注意，修改父类属性，通过子类调用到修改后的属性
# 资源：指是非私有属性与方法
#除了私有属性，保护属性与共有属性及内置属性与方法均可以被继承

# 通过__bases__查看继承的父类
class Person:
    pass
class Mom:
    pass

class Son(Person,Mom):
    pass
print(Person.__bases__)   #查看继承的父类   (<class 'object'>,)
print(Person.__class__)   #查看由什么类创建的   <class 'type'>
print(Son.__class__)      #查看由什么类创建的   <class 'type'>
print(Son.__bases__)      #查看继承的父类  (<class '__main__.Person'>, <class '__main__.Mom'>)

print(type.__class__)
print(type.__bases__)     #type 继承object类

# 资源的影响：
# 1.多个父类方法相同
# 2.与父类有相同的方法
# 3.资源的累加



# 子类属性的修改不会影响到父类的属性值，示例如下：
class Leader:
    age = 50

class Worker(Leader):
    pass


print(Worker.age)
Worker.age = 24
print(Leader.age)
print(Worker.age)

print('-----------------super()------------------')
# super()使用注意事项：
# 一则：不用这样用super(self.__class__,self).__init__()
# 二则：不用使用类调用父类资源，即使用‘父类.__init__’，也不要使用类与super的混合调用
class D:
    def __init__(self):
        print('d')

class B(D):
    def __init__(self):
        # super(self.__class__,self).__init__()   #这种写法容易导致死循环，super的两个参数
        # 第一个是传入当前的结点，第二个参数是查找链，即顺着实例的mro往下查找
        super(B, self).__init__()
        print('b')


class A(B):
    def __init__(self):
        super(A,self).__init__()
        print('a')

A()