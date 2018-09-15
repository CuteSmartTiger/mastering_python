# 私有属性
# 私有方法
class Son:
    __name = 'liu'
    def __dance(self):
        pass
    def school(self):
        pass
s=Son()
print(Son.__dict__)

### 信息格式化操作

class Son:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '儿子的姓名{}，儿子的年龄{}'.format(self.name,self.age)

    def __repr__(self):
        return '程序员爸爸'

s=Son('liu',12)
print(str(s))
print(s)
print(repr(s))
# __str__ 面向用户，使用print函数
# __repr__面向程序员，在python解释器中输入示例变量调用，或者repr(s)
# __repr__     模型定以后，数据库查询列表时，可以打印出列表
# __str__       模型定以后，数据库列表查询时，只可以打印对象，而不可以打印出列表




