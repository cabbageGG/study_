#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/23 下午3:32

__author__ = 'li yangjin'

import urllib2, urllib

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

def getPage():
    req = urllib2.Request('http://zentao.develop.com/index.php?m=my&f=index')
    req.headers = headers

    response = urllib2.urlopen(req)

    ret = response.read()

    print ret

    with open('index.html','w') as fn:
        fn.write(ret)
        fn.close()


getPage()



