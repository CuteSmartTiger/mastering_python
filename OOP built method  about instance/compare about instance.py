# 六种比较方法：
class Person:
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __le__(self, other):
        pass
    def __ge__(self, other):
        pass
    def __gt__(self, other):
        pass




print('------------比较方法的补全---------')
import functools
@functools.total_ordering
class Son:
    def __lt__(self, other):
        print('xiaoyu')

    def __eq__(self, other):
        print('eq')

s1 = Son()
s2 = Son()
print(s1 <= s2)
print(Son.__dict__)



print('-----------------上下文的布尔值------------')
class Mom:
    def __init__(self):
        self.age = 20

    def __bool__(self):
        return self.age > 18

m = Mom()
if m:
    print('ooo')