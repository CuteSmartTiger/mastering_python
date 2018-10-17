import socket
# 补充说明：先运行server，在运行client文件

# 定义一个服务器
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP地址与端口
server.bind(('0.0.0.0', 8888))
# 监听
server.listen()
# 接受返回参数sock,addr
sock, addr = server.accept()
print(sock, addr)
# 单次最大接受256字节
data = sock.recv(256)
data = data.decode('utf-8')
print(type(data))
print('客户端说：', data)
server_msg = '客户端说：{0}'.format(data)
# 发送信息给客户端
sock.send(server_msg.encode('utf-8'))
# 关闭sock
sock.close()
# 关闭服务器
server.close()
