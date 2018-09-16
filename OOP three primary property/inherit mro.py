class D:
    pass

class B(D):
    pass

class C(D):
    pass

class A(B,C):
    pass

# 查看继承顺序
print(A.mro())
print(A.__mro__)
import inspect
print(inspect.getmro(A))
# (<class '__main__.A'>, <class '__main__.B'>,
# <class '__main__.C'>, <class '__main__.D'>,
# <class 'object'>)


# ```
# L（子类（父类1，父类2）） = [ 子类 + merge（ L（父类1） ,  L（父类2） ,  [父类1，父类2] ）]
# L（object） = [ object ]
# + 代表合并列表
# merge算法：
# 1.第一个列表的第一个元素是后续列表(除去第一个列表的其他列表可以看做一个后续列表)的第一个元素
#     或者    后续列表中没有再次出现
#     则将这个元素合并到最终的解析列表中
#     并从当前操作的解析列表中删除
# 2.若不符合，则跳过此元素，查找下一个列表中的第一个元素，重复1的判断
# 3.若最终没法讲所有元素归并到解析列表，则报错
#```
class D(object):
    pass
#  L(D(object)) = [D] + merge(L(object),[object])
#                = [D]+ merge([object],[object])
#               =[D,object]
class B(D):
    pass
# L(B(D)) = [B] + merge(L(D),[D])
#         = [B] +merge([D,object],[D])
#         =[B,D] +merge([object])
#         =[B,D,object]


class C(D):
    pass
# L(C(D)) = [[C,D,object]

class A(B,C):
    pass
# L(A(B,C))=[A]+merge(L(B),L(C),[B,C])
#          =[A]+merge([B,D,object],[C,D,object],[B,C])
#          =[A,B] +merge([D,object],[C,D,object],[C])
#          =[A,B,C] +merge([D,object],[D,object])
#          =[A,B,C,D] +merge([object],[object])
#          =[A,B,C,D,object]
