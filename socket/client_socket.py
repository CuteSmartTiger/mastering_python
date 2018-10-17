import socket
# 补充说明：先运行server，在运行client文件

# 定义一个客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 链接服务器
client.connect(('127.0.0.1', 8888))
# 给服务器发送信息,字节形式
client.send('www.google.com'.encode('utf-8'))
data = client.recv(256)
print('服务器说：', data.decode('utf-8'))
client.close()
