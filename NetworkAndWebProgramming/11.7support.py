from multiprocessing.connection import Client
c = Client(('localhost', 25000), authkey=b'peekaboo')
c.send('hello')
print(c.recv())
# hello
c.send(42)
print(c.recv())
# 42
c.send([1, 2, 3, 4, 5])
print(c.recv())