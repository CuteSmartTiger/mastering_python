# pyhton2.x:
# 方法比较成旧


print('-----------------针对对象的切片操作-----------------')
# python3.x
class Mom:
    # 实例初始化时创建一个空的列表用于后续存储信息，只可以用于修改而不可以增加
    def __init__(self):
        self.cache = [1,2,3,4,5,6,7]

    def __setitem__(self, key, value):
        # self.cache[key] = value
        # 对传入的key进行判断，容错处理
        if isinstance(key,slice):
            self.cache[key.start:key.stop:key.step] = value

    def __getitem__(self, item):
        return self.cache[item]

    def __delitem__(self, key):
        del self.cache[key]

m = Mom()
m[0:5:2]=['A','N','G']
print(m[0:5:2])    #['A', 'N', 'G']
print(m.cache)     #['A', 2, 'N', 4, 'G', 6, 7]
del m[0:5:2]
