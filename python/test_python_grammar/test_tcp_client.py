#-*- coding: utf-8 -*-

# author: li yangjin

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1',9999)) #注意传入的是一个tuple

print(s.recv(1024).decode('utf-8'))
for data in [b'AA',b'BB',b'CC']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()