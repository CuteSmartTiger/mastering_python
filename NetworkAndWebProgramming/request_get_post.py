# 11.1. Interacting with HTTP Services As a Client


# 知识点：
# requests 模块的文档（http://docs.python-requests.org)质量很高
# 在要同一个真正的站点进行交互前，先在 httpbin.org 这样的网站上做实验常常是可取的办法
#json 格式是单引号，不可以写成双引号

import requests
r = requests.get('http://httpbin.org/get?name=Dave&n=37',headers = { 'User-agent': 'goaway/1.0'})

##原版错误之处，json()括号
resp = r.json()
print(resp)


print(resp['headers'])
print(resp['args'])

# url = 'http://httpbin.org/post'
# files = { 'file': ('data.csv', open('data.csv', 'rb')) }
# r = requests.post(url, files=files)


resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
# last_modified = resp.headers['last-modified']
# content_type = resp.headers['content-type']
# content_length = resp.headers['content-length']

# 301 redirect: 301 代表永久性转移(Permanently Moved)，
# 302 redirect: 302 代表暂时性转移(Temporarily Moved )，
print(status)  #301

# print(last_modified)
# print(content_length)
# print(content_type)




####### post ------如果有更复杂的请访问（https://pypi.python.org/pypi/requests）
import requests
# Base URL being accessed
url = 'http://httpbin.org/post'
# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}
# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}
resp = requests.post(url, data=parms, headers=headers)
# Decoded text returned by the request
text = resp.text
print(text)
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "name1": "value1",
#     "name2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Content-Length": "25",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "Spam": "Eggs",
#     "User-Agent": "none/ofyourbusiness"
#   },
#   "json": null,
#   "origin": "47.88.226.161",
#   "url": "http://httpbin.org/post"
# }
