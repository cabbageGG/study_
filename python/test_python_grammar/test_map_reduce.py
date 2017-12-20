#-*- coding: utf-8 -*-

# author: li yangjin
from functools import reduce

def normalize(value):
    return value[0].upper() + value[1:].lower()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

def prod(L):
    return reduce(lambda x,y:x*y,L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

dig = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}

def str2float(s):
    s = s.split('.')
    s1 = s[0]
    if len(s)>1:
        s2 = s[1]
        s2 = s2[::-1]
    else:
        s2 = "0"
    print (s1,s2)
    return reduce(lambda x,y:x*10+y, map(lambda x:dig[x],s1)) + reduce(lambda x,y:x*0.1+y, map(lambda x:dig[x],s2)) * 0.1

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
