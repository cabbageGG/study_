#!/bin/env python
# -*- coding:utf-8 -*-

import re, urllib2, urllib
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context   # 解决错误：URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)>
url = 'https://kyfw.12306.cn/otn/leftTicket/init'

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
            
data = {
    "leftTicketDTO.train_date":"2017-10-20",
    "leftTicketDTO.from_station":"GZQ",
    "leftTicketDTO.to_station":"WHN",
    "purpose_codes":"ADULT"
}

headers = {
    'User-Agent':User_Agent,
    'Host':'kyfw.12306.cn',
    'Referer':'https://kyfw.12306.cn/otn/leftTicket/init'
    }

post_data = urllib.urlencode(data)

request = urllib2.Request(url, post_data, headers)
respones = urllib2.urlopen(request)
result = respones.read().decode('utf-8')
print result




