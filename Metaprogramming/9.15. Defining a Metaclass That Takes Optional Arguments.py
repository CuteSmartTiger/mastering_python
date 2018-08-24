# 9.15. Defining a Metaclass That Takes Optional Arguments

# 目的：定义一个元类，允许类定义时提供可选参数，这样可以控制或配置类型的创建过程
# 强制关键字参数

# 关键之中的关键：弄懂类创建的所有步骤
class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        pass
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        pass
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        pass
        super().__init__(name, bases, ns)

# 当我们构造元类的时候，通常只需要定义一个 __new__() 或 __init__() 方法，
# 但不是两个都定义。 但是，如果需要接受其他的关键字参数的话，这两个方法就
# 要同时提供，并且都要提供对应的参数签名


# 2.补充
# 使用关键字参数配置一个元类还可以视作对
# 类变量的一种替代方式。
class Spam(metaclass=MyMeta):
    debug = True
    synchronize = True
    pass

# 将这些属性定义为参数的好处在于它们不会污
# 染类的名称空间， 这些属性仅仅只从属于类的
# 创建阶段，而不是类中的语句执行阶段


