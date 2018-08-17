from socket import socket, AF_INET, SOCK_STREAM
# 实例化客户端，发信息给服务器
s = socket(AF_INET, SOCK_STREAM)
# 连接服务器
s.connect(('127.0.0.1', 5000))

print(s.send(b'Hello'))

print(s.recv(8192))