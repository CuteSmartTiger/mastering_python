# 统计一个类拥有的实例数量
class Student:
    __student_count = 0
    def __init__(self):
        Student.__student_count +=1
        # print('当前实例数量{}'.format(Student.__student_count))
        print('实例数量+1')

    def __del__(self):
        Student.__student_count -= 1
        # print('当前实例数量{}'.format(self.__class__.__student_count))
        print('实例数量 -1')

    @classmethod
    def total(cls):
        print('当前实例数量{}'.format(cls.__student_count))


print('---1---')
p1=Student()

print('---2---')
p2 = Student()
p3 = Student()
print('---3---')
del p1

print('---4---')
Student.total()

print('---5---')

# ---1---
# 实例数量+1
# ---2---
# 实例数量+1
# 实例数量+1
# ---3---
# 实例数量 -1
# ---4---
# 当前实例数量2
# ---5---
# 实例数量 -1
# 实例数量 -1