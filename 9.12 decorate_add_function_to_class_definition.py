#装饰器对类进行打补丁或者说对类的功能进行扩充

def log_getattribute(cls):
    # Get the original implementation
    orig_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)

    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls

# Example use
@log_getattribute
class A:
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass

a=A(42)
print(a.x)
# getting: x
# 42

print(a.spam)
# getting: spam
# <bound method A.spam of <__main__.A object at 0x00000276526EEE80>>

print(a.spam())
# getting: spam
# None

# 使用继承同样可以得到以上结果，然而
# 类装饰器方案就显得更加直观，并且它不会引
# 入新的继承体系。它的运行速度也更快一些，
# 因为他并不依赖 super() 函数