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
