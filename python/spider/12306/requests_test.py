#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/30 上午9:40

__author__ = 'li yangjin'

import requests, json, logging, os
from requests import Request, Session


requests.packages.urllib3.disable_warnings() #屏蔽掉ssl警告

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

s = requests.Session()

s.headers = headers

def getcode():
    print '>>>begin getcode'
    url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
    r = s.get(url, timeout=5, verify=False) # verify=False 是为了https请求不验证证书ssl
    cookie = r.cookies
    print 'cookie: %s' % cookie
    headers = r.headers
    print 'headers: %s' % headers
    if r.status_code == 200:
        with open('out.png', 'wb') as fp:
            fp.write(r.content)
        print 'getCode success'
    else:
        print 'getCode fail status_code %d != 200' % r.status_code

def uamtk():
    print '>>>begin uamtk'
    url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
    data = {
        'appid':'otn',
    }
    r = s.post(url, data=data, timeout=5, verify=False)
    cookie = r.cookies
    print 'cookie: %s' % cookie
    headers = r.headers
    print 'headers: %s' % headers
    content = r.content
    print 'uamtk return : %s' % content
    global tk
    ret = r.json()
    tk = ret.get('newapptk','')
    print 'tk is : %s' % tk

def uamauthclient():
    print '>>>begin uamauthclient'
    url = 'https://kyfw.12306.cn/otn/uamauthclient'
    global tk
    data = {
        'tk': tk,  #关键点 tk参数怎么来的
    }
    r = s.post(url, data=data, timeout=5, verify=False)
    cookie = r.cookies
    print 'cookie: %s' % cookie
    headers = r.headers
    print 'headers: %s' % headers
    content = r.content
    print 'uamauthclient return : %s' % content

def login():
    getcode()
    code = raw_input('请输入验证码：')
    print '>>>begin check code'
    url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
    data = {
        'answer': code,
        'login_site':'E',
        'rand':'sjrand',
    }
    r = s.post(url, data=data, timeout=5, verify=False)
    cookie = r.cookies
    print 'cookie: %s' % cookie
    headers = r.headers
    print 'headers: %s' % headers
    ret = r.json()
    if ret['result_code'] == '4':
        print 'check code success--msg: %s' % ret['result_message']
        print '>>>begin login'
        login_url = 'https://kyfw.12306.cn/passport/web/login'
        from password import paw
        data = {
            'username':'13246856469',
            'password':paw,
            'appid':'otn',
        }
        r = s.post(login_url, data=data, timeout=5, verify=False)
        cookie = r.cookies
        print 'cookie: %s' % cookie
        content = r.content
        print 'login return content :%s' % content
        ret = json.loads(content)
        print ret
        if ret['result_code'] == 0:
            print 'login success'
            uamtk()
            uamauthclient()
            return True
        else:
            print 'login fail'
            return False
    else:
        print 'check code fail'
        return False

def queryTrainlog():
    print '>>>>>>>>>>>begin queryTrainlog'
    url = 'https://kyfw.12306.cn/otn/leftTicket/log?leftTicketDTO.train_date=2017-11-02&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT'
    r = s.get(url, timeout=3, verify=False)

    ret = r.json()
    print ret

def queryTrain():
    print '>>>>>>>>>>>begin queryTrain'
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-02&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT'
    r = s.get(url, timeout=3, verify=False)

    ret = r.json()
    train_list = ret['data']['result']
    print 'query result: %s' % train_list
    global Train_info
    # Train_info = train_list[3].split('|')
    for i in train_list:
        t_list = i.split('|')
        if t_list[28] == u'有':
            Train_info = t_list
            return True
    return False

def checkUser():
    print '>>>begin check user'
    url ='https://kyfw.12306.cn/otn/login/checkUser'
    r = s.get(url, timeout=5, verify=False)
    cookie = r.cookies
    print 'cookie: %s' % cookie
    headers = r.headers
    print 'headers: %s' % headers
    ret = r.json()
    content = r.content
    print 'check user return content :%s' % content
    if ret['data']['flag']:
        print 'check user success'
    else:
        print 'check user fail'


def submitOrderRequest():
    print '>>>>>>>>begin submitOrderRequest'
    url = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
    global Train_info
    if Train_info is None:
        print 'Train_info is None'
        return
    secretStr = Train_info[0]
    #print type(secretStr),secretStr
    s_str = secretStr.encode('unicode-escape').decode('string_escape')
    #print type(s_str),s_str
    data = {
      'secretStr': s_str,
      'train_date': '2017-11-02',
      'back_train_date': '2017-11-02',
      'tour_flag': 'dc',
      'purpose_codes': 'ADULT',
      'query_from_station_name': '长沙',
      'query_to_station_name': '成都',
      'undefined': '',
    }  # secretStr 怎么来的？ 是不是md5拼出来的？
       # a:不是，是该页面预定按钮对应的js字符串。可从页面获取        XX 错误分析 XX
       # a: 没有这么复杂，直接可以从查询请求获得的data参数里的第一个参数就是。query_to_station_name=%E6%88%90%E9%83%BD
    print 'data: %s' % data
    # new_data = json.dumps(data, ensure_ascii=False)
    # c = requests.cookies.RequestsCookieJar()
    # c.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')
    # s.cookies.update(c)
    # s.cookies['_jc_save_fromStation'] = '%u957F%u6C99%2CCSQ'
    # s.cookies['_jc_save_toStation'] = '%u6210%u90FD%2CCDW'
    # s.cookies['_jc_save_fromDate'] = '2017-11-02'
    # s.cookies['_jc_save_toDate'] = '2017-11-02'
    # s.cookies['_jc_save_wfdc_flag'] = 'dc'

    r = s.post(url, data=data, timeout=5, verify=False)
    req = r.request.headers
    print 'headers: %s' % req
    req = r.request.body
    print 'req: %s' % req
    req = r.request.url
    print 'req: %s' % req
    content = r.content
    print 'submitOrderRequest return : %s' % content


def get_passengers():
    print u'=====>>>>正在获取联系人...'
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
    parameters = {
        '_json_att': '',
    }
    r = s.post(url, parameters, timeout=5, verify=False)
    assert r.status_code == 200
    resp = r.json()
    headers = r.headers
    print 'headers: %s' % headers
    cookie = r.cookies
    print 'cookie: %s' % cookie
    print 'passengers: %s' % resp
    print 'msg:%s' % resp['data']['exMsg']

def hard_requests():
    url = 'http://www.baidu.com'
    s = Session()
    data = {
        'aa': '暗暗',
    }
    req = Request('POST', url, data=data )

    prepped = req.prepare()
    print prepped.url
    print prepped.body
    print prepped.headers

    resp = s.send(prepped)

global Train_info
global html
global token
global tk

if __name__ == '__main__':
    global Train_info
    Train_info = []
    # if login():
    #     if queryTrain():
    #         print '有票'
    #         print Train_info
    #         checkUser()
    #         submitOrderRequest()
    #     else:
    #         print '无票'
    #hard_requests()
    #submitOrderRequest()
    queryTrainlog()


