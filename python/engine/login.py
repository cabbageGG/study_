#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/21 下午2:24

__author__ = 'li yangjin'

import urllib, urllib2

import ssl, cookielib, json, time

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)  # urlopne 默认使用 全局opener

def login():
    req = urllib2.Request('http://zentao.develop.com/index.php?m=user&f=login&referer=Lw==')
    req.headers = headers
    data = {
        'account': 'yangjin',
        'password': 'yangjin',
        'referer': '/',
    }

    data = urllib.urlencode(data)

    response = urllib2.urlopen(req, data=data)

    if response.getcode() == 200:
        print '请求成功'

    ret = response.read()

    ret = ret + '\n' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n'

    print ret

    with open('login.log', 'a') as fn:
        fn.write(ret)

login()


