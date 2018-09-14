# 对象存储


# 引用计数
import sys
class Son:
    pass

p=Son()
print(p)
print(id(p))
print(sys.getrefcount(p))
p1 = p

print(hex(id(p1)))
print(sys.getrefcount(p))

# 引用计数加的场景：
# 被引用，作为参数传递，作为容器中的值

# 引用计数减的场景：
# 对象别名赋予新的对象，对象别名被显示销毁，一个对象离开他
# 的作用域，对象所在的容器被销毁或者容器中的对象被删除