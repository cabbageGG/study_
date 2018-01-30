#!/bin/env python
# -*- coding:utf-8 -*-

import re, urllib2, urllib
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context   # 解决错误：URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)>
url = 'https://kyfw.12306.cn/otn/leftTicket/query'

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
            
headers = {
    'User-Agent':User_Agent,
    }

query_parameters = "?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=%s" % ("2017-12-20","GZQ","WHN","ADULT")
get_url = url + query_parameters
print get_url

request = urllib2.Request(get_url, headers=headers)

respones = urllib2.urlopen(request)
result = respones.read()
print result




