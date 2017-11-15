#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/21 上午10:32

__author__ = 'li yangjin'

import urllib, urllib2

import ssl, cookielib, json

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener) # urlopne 默认使用 全局opener

def getcode():
    req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.9730617288073076')
    req.headers = headers
    response = urllib2.urlopen(req)
    print response.getcode()
    # print response.read()
    file = response.read()
    with open('out.png','wb') as fn:
        fn.write(file)

def login():
    getcode()
    print '请输入验证码：'
    code = raw_input()

    req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
    req.headers = headers
    data = {
        'answer': code,
        'login_site':'E',
        'rand':'sjrand',
    }
    data = urllib.urlencode(data)
    response = urllib2.urlopen(req, data=data)

    #print response.read()  # 注意：这里response.read() 只能执行一次

    str1111 = response.read()

    print str1111

    result = json.loads(str1111)
    print result

    if result['result_code'] == '4':
        print '开始登陆'
        req_login = urllib2.Request('https://kyfw.12306.cn/passport/web/login')
        req_login.headers = headers
        from password import paw
        data = {
            'username':'13246856469',
            'password':paw,
            'appid':'otn',
        }
        data = urllib.urlencode(data)
        res_login = urllib2.urlopen(req_login, data=data)
        print res_login.read()
    else:
        print '验证码校验失败'
        login()


login()



