# 11.7. Communicating Simply Between Interpreters
# 目的：在不同的机器上面运行着多个Python解释器实例，并希望能够在这些解
# 释器之间通过消息来交换数据。

from multiprocessing.connection import Listener
import traceback

# 与客户端的连接
def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')


def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 25000), authkey=b'peekaboo')