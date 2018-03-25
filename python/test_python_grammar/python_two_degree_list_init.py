#-*- coding: utf-8 -*-
'''
使用双列表生成式，初始化python二维数组
'''
a = [[0 if col!=0 else 8 for col in range(3)] for row in range(4)]
print(a)
a[0] = [1,2,3]
print(a)
