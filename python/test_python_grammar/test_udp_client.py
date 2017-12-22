#-*- coding: utf-8 -*-

# author: li yangjin

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1",9999)
for data in [b'AA',b'BB']:
    s.sendto(data,addr)
    print(s.recv(1024).decode('utf-8'))
s.close()