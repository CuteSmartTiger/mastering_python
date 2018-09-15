print('----------------实例对象的索引操作--------------------')
# 定义__setitem__，__getitem__，__delitem__,可以像操作字典一样，操作实例对象
class Mom:
    # 实例初始化时创建一个空的字典用于后续存储信息
    def __init__(self):
        self.cache = {}

    def __setitem__(self, key, value):
        self.cache[key] = value

    def __getitem__(self, item):
        return self.cache[item]

    def __delitem__(self, key):
        del self.cache[key]

m = Mom()
m['name']='nana'
print(m['name'])
del m['name']
