#-*- coding: utf-8 -*-

# author: li yangjin

def consumer():
    r = '' # 2
    while True:
        n = yield r #3
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) #1
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) #4
        print('[PRODUCER] Consumer return: %s' % r)
    c.close() #5

c = consumer()
produce(c)