#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/22 下午3:06

__author__ = 'li yangjin'

import urllib2,urllib

import ssl, json

ssl._create_default_https_context = ssl._create_unverified_context


headers = {
   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

def queryTrain():
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-10-26&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT')
    req.headers = headers

    response = urllib2.urlopen(req)

    result = response.read()

    print type(result)

    res_json = json.loads(result)

    train_list = res_json['data']['result']

    print type(train_list)

    index = 0

    for i in train_list:
        t_list = i.split('|')
        for t in t_list:
            print '[%s] %s' % (index, t)
            index += 1
        break

queryTrain()



