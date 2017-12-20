#-*- coding: utf-8 -*-

# author: li yangjin

def test_params(*args,**kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    pass

test_params(1,2,3,a=1,b=2,c=3)
# test_params(1,d=2,3,a=1,b=2,c=3) #错误示例

a = [1,2,3]
b = (1,2,3)
c = {"a":1,"b":2,"c":3}
test_params(a,c)
test_params(b,c)
test_params(*a,**c)
test_params(*b,**c)