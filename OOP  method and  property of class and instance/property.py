# 只读属性：
# 方法一：
class Person:
    def __init__(self):
        self.__name = 21

    @property
    def age(self):
        print('---get---')
        return self.__name

    @age.setter
    def age(self,value):
        print('--set--')
        self.__name = value



p = Person()
print(p.age)
# p.age = 12     #@property,添加后只读，不可以赋值
p.age = 13
print(p.age)
# 推荐使用新式类，经典类中p.age会新增属性，而不能关联到原有的属性
print(p.__dict__)  #{'_Person__name': 13},


print('------------------------------2------------------------')
# 方法二：
# 设置指定属性只读
class Per:
    def __setattr__(self, key, value):
        print(key,value)
        if key == 'age' and key in self.__dict__.keys():
            print('不能修改')
        else:
            # 陷入死循环
            # self.key = value
            print('fuzhi')
            self.__dict__[key] = value

x = Per()
x.age =15
print(x.__dict__)
print(x.age)

x.age = 20
print(x.age)
print(x.__dict__)

# 通过修改实例属性字典
x.__dict__['age'] = 19
print(x.age)