#-*- coding: utf-8 -*-

# author: li yangjin

import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print("hello")
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print("2017-12-20")

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('hello，%s' % text)
            return func(*args, **kw)
        return wrapper
    return decorator


@log('Bob')
def now():
    print('2017-12-20')


now()

