# 从client导入服务器代理
from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:15000', allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
print(s.keys())
# ['foo', 'spam']
print(s.get('foo'))
# bar
print(s.get('spam'))
# [1, 2, 3]
s.delete('spam')
print(s.exists('spam'))
# False


