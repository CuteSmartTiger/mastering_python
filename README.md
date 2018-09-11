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


用法：
__init__
__new__
__member__
__gettr__
__call__
__repr__     列表查询时，可以打印出列表
__str__      列表查询时，只可以打印对象，而不可以打印出列表
__set__
__delete__

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