#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/25 上午9:16

__author__ = 'li yangjin'

from bs4 import BeautifulSoup
import re, json
import requests
from requests import Request, Session

# with open('initDc.html', 'r') as f:
#     html = f.read()
#
# token = re.split('\'', re.search('.+globalRepeatSubmitToken.+?;', html).group())
# print token[1]


def submitOrderRequest():
    print '>>>>>>>>begin submitOrderRequest'
    url = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
    # global Train_info
    # if Train_info is None:
    #     print 'Train_info is None'
    #     return
    data = {
      'train_date':'2017-11-02',
      'back_train_date':'2017-11-02',
      'tour_flag': 'dc',
      'purpose_codes': 'ADULT',
      'query_from_station_name': '长沙',
      'query_to_station_name': '成都',
      'undefined': '',
    }  # secretStr 怎么来的？ 是不是md5拼出来的？
       # a:不是，是该页面预定按钮对应的js字符串。可从页面获取        XX 错误分析 XX
       # a: 没有这么复杂，直接可以从查询请求获得的data参数里的第一个参数就是。
    print 'data: %s' % data
    new_data = json.dumps(data, ensure_ascii=False)
    print 'new_data: %s' % new_data


#submitOrderRequest()

aa = u'%E6%88%90%E9%83%BD'

print aa.encode('utf-8')






