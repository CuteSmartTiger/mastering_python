# 11.9. Authenticating Clients Simply

import hmac
import os

# 1.服务器端发送随机组成的信息message
# 2.客户端接受信息然后加密处理得digest，然后发送给服务器
# 3.服务器同时用相同的加密算法得打digest
# 4.服务器端收到客户端发过的digest记为response，然后进行比较

def server_authenticate(connection, secret_key):
    '''
    Request client authentication.
    '''
    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest,response)

# 创造网络或消息处理的代码，以便使用上面的函数
from socket import socket, AF_INET, SOCK_STREAM

secret_key = b'peekaboo'
def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        client_sock.close()
        return
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        c,a = s.accept()
        echo_handler(c)

echo_server(('', 18000))



