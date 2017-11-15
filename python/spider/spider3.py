#!/bin/env python
# -*- coding:utf-8 -*-

import re, urllib2, urllib
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context   # 解决错误：URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)>
url = 'http://engine.develop.com/'

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
            
# data = {
#     "account":"yangjin",
#     "password":"yangjin",
#     "referer":"/"
# }

headers = {
    'User-Agent':User_Agent,
    'Host':'zentao.develop.com',
    'Referer':'http://zentao.develop.com/index.php?m=user&f=login&referer=Lw==',
    'Origin':'http://zentao.develop.com'
    }

# post_data = urllib.urlencode(data)

request = urllib2.Request(url, headers=headers)
respones = urllib2.urlopen(request)
print respones.getcode()
result = respones.read().decode('utf-8')
print result




