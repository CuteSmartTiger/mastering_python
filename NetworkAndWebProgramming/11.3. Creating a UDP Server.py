# 11.3. Creating a UDP Server

from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        # client_address是个元组('127.0.0.1', 50682)，每一运行时端口会改变
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        print(msg)
        print(sock)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()

# Got connection from ('127.0.0.1', 60752)