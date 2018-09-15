# 实现实例对象的迭代：
# 方法一： for  in   __getitem__

class Son:
    def __init__(self):
        self.res = 0

    def __getitem__(self, item):
        self.res +=1
        if self.res >= 6:
            raise StopIteration('stop')
        return self.res

s = Son()

for i in s:
    print(i)


# 实现实例对象的迭代：
# 方法二： __iter__  __next__

class Son:
    def __init__(self):
        self.res = 0

    # def __getitem__(self, item):
    #     print('getitem')
    #     self.res +=1
    #     if self.res >= 6:
    #         raise StopIteration('stop')
    #     return self.res

    # 利用__iter__产生迭代器,优先级比__getitem__高
    def __iter__(self):
        # 此处赋值，以便可以对实例进行多次迭代，每次调用时对判定条件进行赋值
        self.res = 0
        print('iter')
        # 不是self.res
        return self

    def __next__(self):
        self.res += 1
        if self.res >= 6:
            raise StopIteration('stop')
        return self.res

s = Son()
print('-----------------------------s')
f = iter(s)
for i in f:
    print(i)

print(id(s) == id(f))      #True

print('-----------------------------s')
for i in s:
    print(i)

# 由于在iter中定义了res 的初始值，所以可以多次for in  调用
for i in s:
    print(i)


print('----------next---------')
# 在next()中无法赋值实现迭代器的复用
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# 迭代器：必须同时实现iter与next方法
# 迭代对象：实现iter方法即可
import collections
# 判定是否迭代器
print(isinstance(s,collections.Iterator))
# 判定是否迭代对象
print(isinstance(s,collections.Iterable))


print('---------------iter--------------')
# 会报错，需要定义__call__方法，方可被调用，遇到4终止，4不会被打印
# print(iter(p,4))