#-*- coding: utf-8 -*-

# author: li yangjin

from functools import reduce

def str2num(s):
    try:
        n = int(s)
    except ValueError as e:
        n = float(s)
    return n

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()