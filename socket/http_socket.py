# socket 模拟http请求
# 理解requests urllib socket 之间的关系

import socket
# 导入URL解析函数
from urllib.parse import urlparse


def get_url(url):
    # 解析URL地址
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    # 请求页面
    client.send('GET {0}\r\nHost:{1}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf-8'))
    # 初始化字节信息
    data = b''
    while True:
        d = client.recv(1024)
        # 接受信息，若为空则停止接受，若不为空，则累加
        if d:
            data += d
        else:
            break
    # 信息解码
    data = data.decode('utf-8')
    print(data)
    client.close()


if __name__ == "__main__":
    get_url('http://studyai.com/')
    # get_url('http://www.baidu.com/')
