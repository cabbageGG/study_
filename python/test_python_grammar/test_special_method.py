#-*- coding: utf-8 -*-

# author: li yangjin
class Chain(object):
    def __init__(self, path=''):
        super(Chain, self).__init__()
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    def __call__(self, value):
        return Chain('%s/%s' % (self.__path, value))

print(Chain().status.user.timeline.list)


