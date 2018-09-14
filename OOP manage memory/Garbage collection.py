# 目的是解决循环引用的问题

# 检测流程：
# 步骤：
# 1.收集所有的容器对象，通过双向链表进行引用，而不是非容器对象
# 2.针对每一个容器，通过gc_refs来记录对应引用的引用计数
#3.对于每一个容器，找到他的引用容器对象，将这个容器对象引用计数-1
# 经过以上三步骤，引用计数为0，则可以被回收


# 分代回收：


import gc

gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

print(gc.get_threshold())
gc.set_threshold(700, 10, 10)
# 当计数器从(699,3,0)增加到(700,3,0)，gc模块就会执行gc.collect(0),即检查0代对象的垃圾，并重置计数器为(0,4,0)
# 当计数器从(699,9,0)增加到(700,9,0)，gc模块就会执行gc.collect(1),即检查0、1代对象的垃圾，并重置计数器为(0,0,1)
# 当计数器从(699,9,9)增加到(700,9,9)，gc模块就会执行gc.collect(2),即检查0、1、2三代对象的垃圾，并重置计数器为(0,0,0)


# 手动触发垃圾回收
gc.collect()

# 如何解决python2.x中的循环引用
# 使用弱引用
import weakref

class Person:
    pass

class Dog:
    pass

p = Person()
d = Dog()
p.pet = d
d.master = weakref.ref(p)

# 其它弱引用：
weakref.WeakKeyDictionary()
weakref.WeakValueDictionary()