from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:15000', allow_none=True)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
s.set('foo', p)
s.get('foo')
# {'x': 2, 'y': 3}