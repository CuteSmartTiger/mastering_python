from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)

print(s.sendto(b'', ('localhost', 20000)))
# 0
print(s.recvfrom(8192))
# (b'Sat Aug 18 00:35:50 2018', ('127.0.0.1', 20000))