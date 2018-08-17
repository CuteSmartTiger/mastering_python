# 11.2. Creating a TCP Server

from socketserver import BaseRequestHandler, TCPServer
# TCP协议是基于服务器与客户端之间发生的。客户端发起请求，
# 与服务器建立连接（一个服务器可以接受多个客户端的连接，
# 一个客户端只能连接一台服务器）

# 单线程

# 本程序为服务端
class EchoHandler(BaseRequestHandler):
    # handle()方法处理客户端的连接
    def handle(self):
        # client_address 为客户端地址
        print('Got connection from', self.client_address)
        while True:
            # 8192代表每次读取8192字节
            msg = self.request.recv(8192)
            print(msg)
            if not msg:
                break
            self.request.send(msg)

if __name__ == '__main__':
    # TCPServer在实例化的时候会绑定并激活相应的socket
    # 想通过设置某些选项去调整底下的socket ，可以设置参数
    bind_and_activate = False
    serv = TCPServer(('127.0.0.1', 5000), EchoHandler)
    # serve_forever(self, poll_interval=0.5),服务器间隔0.5秒重启
    serv.serve_forever()

# Got connection from ('127.0.0.1', 59356)
# b'Hello'
# b''