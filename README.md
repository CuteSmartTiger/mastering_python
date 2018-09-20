# mastering_python


## decorators的深度理解与多种用法
- 1.如何定义一个基本的装饰器并使用，如何保留装饰器的元数据（原信息），为什么需要保留原信
息了，什么场合需要这样做？如何对装饰器进行解包？

- 2.如何定义一个可接受参数的装饰器，如何定义一个属性可由用户修改的装饰器，如何定义一个能
接受可选参数的装饰器，这三者的区别是什么？请结合知识点1一起总结归纳

- 3.如何利用装饰器强制函数上的类型检查？

- 4.在类中定义装饰器，将装饰器定义为类，两者的区别与联系？

- 5.把装饰器作用到类和静态方法上，两者是如何实现的，两者的区别是什么？

- 6.装饰器为被包装函数增加参数，如何实现装饰器对类进行打补丁或者说对类的功能进行扩充，两
者实现方式有何不同，是否还有其他方法可以分别实现他们对应的目的？

查看工具：
__bases__查看继承的父类
__dict__ 查看类或者实例的属性


用法：

__metaclass__
__all__   定义可导入的变量
__init__
__new__
__member__
__gettr__
__call__
__repr__     列表查询时，可以打印出列表
__str__      列表查询时，只可以打印对象，而不可以打印出列表

__set__
__setattr__
__setitem__

区别：
__del__
__delete__
delattr()


@classmethod, @staticmethod


#### __get__,__getattr__和__getattribute都是访问属性的方
- 用法
```
object.__getattr__(self, name)
当一般位置找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。

1. 无论调用对象的什么属性，包括不存在的属性，都会首先调用“_ getattribute_”方法；
2. 只有找不到对象的属性时，才会调用“_ getattr_”方法；

object.__getattribute__(self, name)
无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()
不会被调用（除非显示调用或引发AttributeError异常）

object.__get__(self, instance, owner)
如果class定义了它，则这个class就可以称为descriptor。owner是所有者的类，instance是
访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。
（descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，只有descriptor
作为其它类的属性才有意义。）


“_ getattribute_”只适用于所有的“.”运算符
“_ getitem_”只适用于所有的“[]”运算符补充示例：
```
- 优先级
__getattribute__ > __getattr__



等很多待双下划线的用法

关于属性：
前置单一下划线：受保护的属性
前置双下划线：私有属性，实现的机制为名称重整机制，不同的解释器编译规则不一样，一般是变为_class__name

只读属性：
方法一：先设置为私有属性，然后再部分公开，即内部将值返回，优化方法，增加property装饰器，实现只读，赋值即报错

关于规则：
后置单一下划线：定义变量时添加后单一下划线，用与系统内置名称的区分识别
前后双下划线：系统内建名称，程序开发者要避免使用这种方法

|属性类别|类内部|子类内部|当前模块其他位置|其他模块|备注|
| -----|-----|-----|-----|-----|-----|
|公有属性||||||||全部位置都可以访问|
|受保护属性|可以，受保护区域|可以，受保护区域|访问类或者父类，实例或者子实例，警告|可以访问受保护的变量，但是警告，from module import * 此方法不可以，import module 可以|__all__定义的变量可以访问|
|私有属性|可以|不可以|不可以|类的私有属性不可以访问，但是独立于类外私有变量可以通过import module访问|from module import * 此方法不可以私有变量|