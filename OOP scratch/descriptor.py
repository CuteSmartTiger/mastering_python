# 本节疑点：
# 1.当私有属性不存在时报错，可否将错误信息输出，明文显示
# 2.__weakref__的用法


# 辅助知识点：
# help(Father) 用于查看类的帮助文档，了解帮助文档的分类
# 数据描述器:
# __dict__
# __weakref__
# 非数据描述器


# 基础示例：
class Father:
    def __init__(self):
        self.__age=10

    def get_age(self):
            return self.__age

    def set_age(self,value):
        if value>100:
            print('changshou')
        if value<0:
            value = 0
        self.__age=value

    def del_age(self):
        del self.__age


p = Father()
print(p.get_age())
p.del_age()
p.set_age(18)
print(p.get_age())

print('-----------')
# 描述器的定义方法：方法一
class Father:
    def __init__(self):
        self.__age=10

    def get_age(self):
            return self.__age

    def set_age(self,value):
        if value>100:
            print('changshou')
        if value<0:
            value = 0
        self.__age=value

    def del_age(self):
        del self.__age

    # 此处的age即为描述器,简化调用方法
    age = property(get_age,set_age,del_age)

p = Father()
# 获取
print(p.age)
# 删除
del p.age
# print(p.age)
# 赋值：
p.age = 19
print(p.age)


print('-----------')
# 方法一的优化：
class Father:
    def __init__(self):
        self.__age=10

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if value>100:
            print('changshou')
        if value<0:
            value = 0
        self.__age=value

    @age.deleter
    def age(self):
        del self.__age


p = Father()
# 获取
print(p.age)
# 删除
del p.age
# print(p.age)
# 赋值：
p.age = 19
print(p.age)


# 描述器定义方法二
class Age:

    def __get__(self, instance, owner):
        print('get')

    def __set__(self, instance, value):
        print('set')

    def __delete__(self, instance):
        print('delete')

class Person:
    age=Age()

per = Person()
per.age = 12
print(per.age)
del per.age

print(Person.age)   #可以通过类属性方法调用get方法
Person.age = 14     #不可以通过类属性方法调用set方法
del Person.age     #不可以通过类属性方法调用del方法
# 备注：1.调用描述器使用实例方法而不用类方法

# 不能够顺利转换的两种情况
# 1.描述器只能在新式类中实现，经典类中需要两个类同时继承object才可以实现
#2.调用的顺序：
# 首先，实例对象的自身__dict__字典
# 然后，类对象的自身__dict__字典
# 其次，如果有父类，会往上一层__dict__字典检测
# 最后，若没找到，而又定义了___getattr__方法，则调用这个

# 重写方法覆盖__get__方法
class Person:
    age=Age()
    def __getattribute__(self, item):
        print(13)

per = Person()
per.age = 12
print(per.age)   #13,__getattribute__方法覆盖了__get__方法
del per.age

# 资料描述器  定义了get set 方法
# 非资料描述器 仅仅定义了get 方法

# 方法的调用顺序：
# 资料描述器 > 实例属性 >非资料描述器
print('------------------test----------')
class Person:
    age=Age()
    def __init__(self):
        self.age = 12


pp = Person()    #set,调用资料描述器的方法
print(pp.__dict__)  #{}
pp.age = 13      #set,调用资料描述器的方法
print(pp.age)    #get,调用资料描述器的方法
del pp.age       #delete,调用资料描述器的方法

print('------------------非资料描述器----------')
class Age:
    def __get__(self, instance, owner):
        print('get')

class Person:
    age=Age()
    def __init__(self):
        self.age = 12

pf = Person()
pf.age = 13
print(pf.age)    #13,调用非资料描述器的方法
print(pf.__dict__)    #{'age': 13}
del pf.age



print('-------------where to save data-------')
# 数据存储，让不同的实例对象可以拥有不同的属性值
# 先了解Person 与Age 存储值的位置，代码如下：
class Age:
    def __get__(self, instance, owner):
        print('get')
        return self.va

    def __set__(self, instance, value):
        print('set',self,instance,value)
        self.va = value

    def __delete__(self, instance):
        print('delete')

class Person:
    age=Age()

px = Person()
px.age =11
print(px.age)    #11

pc = Person()
pc.age = 12
print(pc.age)    #12

print(px.age)   #12
# 可见age的属性是共享的
# set <__main__.Age object at 0x0000026203C2BC18> <__main__.Person object at 0x0000026203C2BC50> 11
# set <__main__.Age object at 0x0000026203C2BC18> <__main__.Person object at 0x0000026203C2BCC0> 12

print('-------------youhua----------')
# 可见person类对象的存储位置不一样，将属性值与person类绑定，即与instance所以优化如下：
class Age:
    def __get__(self, instance, owner):
        print('get')
        return instance.va

    def __set__(self, instance, value):
        print('set',self,instance,value)
        instance.va = value

    def __delete__(self, instance):
        print('delete')
        del instance.va

class Person:
    age=Age()

px = Person()
px.age =11
print(px.age)   #11

pc = Person()
pc.age = 12
print(pc.age)   #12

print(px.age)   #11
