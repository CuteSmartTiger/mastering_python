# 想要并发操作，可以实例化一个 ForkingUDPServer 或 ThreadingUDPServer 对象：
# from socketserver import ThreadingUDPServer
#
#    if __name__ == '__main__':
#     serv = ThreadingUDPServer(('',20000), TimeHandler)
#     serv.serve_forever()

# 直接使用 socket 来实现一个UDP服务器也不难，下面是一个例子：

from socket import socket, AF_INET, SOCK_DGRAM
import time

def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)

if __name__ == '__main__':
    time_server(('', 20000))