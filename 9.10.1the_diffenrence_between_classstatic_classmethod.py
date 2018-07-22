# classmethod方法解析
# @classmethod @staticmethod区别
class A(object):
    bar = 1
    def func1(self):
        print ('foo')
        return "nice"

    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()
        return "thanks"


a=A()
print(A.func2())

