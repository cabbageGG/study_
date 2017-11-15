#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/23 下午4:46

__author__ = 'li yangjin'

import urllib, urllib2

import ssl, cookielib, json

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)  # urlopne 默认使用 全局opener

def login():
    req1 = urllib2.Request('http://zentao.develop.com/index.php?m=user&f=login&referer=Lw==')
    req1.headers = headers
    data = {
        'account': 'yangjin',
        'password': 'yangjin',
        'referer': '/',
    }

    data = urllib.urlencode(data)

    res1 = urllib2.urlopen(req1, data=data)

    if res1.getcode() == 200:
        print '请求成功'
        return True
    else:
        print '失败'
        return False





def getPage():
    req = urllib2.Request('http://zentao.develop.com/index.php?m=my&f=index')
    req.headers = headers

    response = urllib2.urlopen(req)

    ret = response.read()

    print ret

    with open('index.html','w') as fn:
        fn.write(ret)
        fn.close()


def test():
    print '测试开始'
    isLogin = login()
    if isLogin:
        getPage()

    print '测试结束'

test()
