# 6.2. Reading and Writing JSON Data

# json与python数据结构的转换

# 针对文字的操作,dumps,loads
import json
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
print(json_str)
data1 = json.loads(json_str)
print(data1)


# 针对文件操作dump，load,文件如没有，则创建
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data2 = json.load(f)
    print(data2)

with open('data.txt', 'w') as f:
    json.dump(data, f)

# 知识点：
# JSON编码支持的基本数据类型为 None ， bool ， int ， float 和 str ，
# 以及包含这些类型数据的lists，tuples和dictionaries。 对于dictionaries，
# keys需要是字符串类型(字典中任何非字符串类型的key在编码时会先转换为字符串)
d = {'a': True,'b': 'Hello','c': None,'d':False}
print(json.dumps(d))
# json会将大写转换为小写
# {"a": true, "b": "Hello", "c": null, "d": false}

# 当数据的嵌套结构层次很深或者包含大量的字段时，打印来确定它的结构
# import requests
# resp = requests.get('https://api.github.com/events')
# data_json = resp.json()
# print(data_json)
# from urllib.request import urlopen
# import json
# u = urlopen('https://api.github.com/events')
# resp = json.loads(u.read().decode('utf-8'))
# from pprint import pprint
# pprint(resp)


s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# 将一个JSON字典转换为一个Python对象例子
class JSONObject:
     def __init__(self, d):
         self.__dict__ = d
data = json.loads(s, object_hook=JSONObject)
print(data.name,data.shares,data.price)


data = {"name": "ACME", "shares": 50, "price": 490.1}
# 使用indent让输出格式更好看
print(json.dumps(data, indent=4))
# {
#     "name": "ACME",
#     "shares": 50,
#     "price": 490.1
# }
