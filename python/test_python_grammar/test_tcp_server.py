#-*- coding: utf-8 -*-

# author: li yangjin

import socket,threading,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9999)) #注意，传入一个tuple

s.listen(5)  #传入的参数指定等待连接的最大数量

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!') #以字节的形式发送,b
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit': #设置通信截止符号 ‘exit'
            break
        sock.send(b'Hello, %s!' % data.decode('utf-8').encode('utf-8')) #自动回复。注意，编码解码！！
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock,addr = s.accept() #这里会阻塞吧
    t = threading.Thread(target=tcplink, args=(sock,addr))
    t.start()

