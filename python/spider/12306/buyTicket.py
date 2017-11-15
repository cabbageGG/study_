#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/22 下午3:28

__author__ = 'li yangjin'

import urllib2,urllib

import ssl, json, cookielib

ssl._create_default_https_context = ssl._create_unverified_context  #解决证书不安全问题


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


def checkUser():
    req1 = urllib2.Request('https://kyfw.12306.cn/otn/login/checkUser')
    req1.headers = headers
    res1 = urllib2.urlopen(req1)

    ret1 = res1.read()

    print ret1

#关键 点击预定车票
def submitOrderRequest():
    req2 = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest')
    req2.headers = headers
    data = {
      'secretStr':'3aySbChYtwyFRVzderifFtEbDJm2a1NCVywWiSVbrQnmTI6ZW/CMFy4aD4+LUG7arZbtMDS1w3KvSil8qg4+ZzyIxUeoLSjJr840uXdhK9HEX4WfJEXYmFQbIUlH2Z2jGE1kk//ww+993scdZRvWfR1FQG2Y0XjCHFwrGXFVryXG38c85XPMCRCRG7RvyW7KiEg6TElToFzvfIp1dyMUJ+xV1TNJo+QiQNIi0vqwaKlv8bdo',
      'train_date':'2017-10-26',
      'back_train_date':'2017-10-22',
      'tour_flag':'dc',
      'purpose_codes':'ADULT',
      'query_from_station_name':'长沙',
      'query_to_station_name':'成都',
      'undefined':'',
    }  # secretStr 怎么来的？ 是不是md5拼出来的？
       # a:不是，是该页面预定按钮对应的js字符串。可从页面获取        XX 错误分析 XX
       # a: 没有这么复杂，直接可以从查询请求获得的data参数里的第一个参数就是。

    data = urllib.urlencode(data)

    res2 = urllib2.urlopen(req2, data=data)

    ret2 = res2.read()

    print ret2

#getToken
def initDc():
    req3 = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/initDc')
    req3.headers = headers
    data = {
        '_json_att':'',
    }

    data = urllib.urlencode(data)

    res3 = urllib2.urlopen(req3, data=data)

    ret3 = res3.read()

    print ret3

#关键 有返回值 可选乘客信息
def getpassengerInfo():
    req3 = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs')
    req3.headers = headers
    data = {
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':'5ed1a56b8191cfcdc49e45eadbaa28f9',
    } # REPEAT_SUBMIT_TOKEN 这个token 怎么得来的？
      # a: token 可以从前面初始化的页面initDc里拿到
      # 如： var globalRepeatSubmitToken = '35753d91155b9fdc35a4142018f3d6e3';

    data = urllib.urlencode(data)

    res3 = urllib2.urlopen(req3, data=data)

    ret3 = res3.read()

    print ret3

#关键 点击提交订单
def checkOrderInfo():
    req4 = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo')
    req4.headers = headers
    data = {
        'cancel_flag':'2',
        'bed_level_order_num':'000000000000000000000000000000',
        'passengerTicketStr':'3,0,1,李阳进,1,420107199204250511,,N',
        'oldPassengerStr':'李阳进,1,420107199204250511,1_',
        'tour_flag':'dc',
        'randCode':'',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':'5ed1a56b8191cfcdc49e45eadbaa28f9',
    } #  上面order参数 是怎么填的，分析规则？？

    data = urllib.urlencode(data)

    res4 = urllib2.urlopen(req4, data=data)

    ret4 = res4.read()

    print ret4

# 查询当前车次余票
def getTicketsCount():
    req5 = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount')
    req5.headers = headers
    data = {
        'train_date': 'Thu Oct 26 2017 00:00:00 GMT+0800 (CST)',
        'train_no':'630000Z12208',
        'stationTrainCode':'Z122',
        'seatType':'3',
        'fromStationTelecode':'CSQ',
        'toStationTelecode':'CDW',
        'leftTicket':'F%2FAJmwDx4QSPTfxEHgmaphlGo1MdX64auXkCXVHwkco6ULzOm1K%2B5CaQ1Js%3D',
        'purpose_codes':'00',
        'train_location':'Q9',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':'5ed1a56b8191cfcdc49e45eadbaa28f9',
    } # 上面ticket参数 是怎么填的，分析规则？？ leftTicket是什么东西
      # a: 在initDc 获得的网页里 可以找到leftTicketStr字段

    data = urllib.urlencode(data)

    res5 = urllib2.urlopen(req5, data=data)

    ret5 = res5.read()

    print ret5

# 点击确认之后 请求
def confirmSingelForQueue():
    req6 = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue')
    req6.headers = headers
    data = {
        'passengerTicketStr': '3, 0, 1, 李阳进, 1, 420107199204250511,, N',
        'oldPassengerStr':'李阳进, 1, 420107199204250511, 1_',
        'randCode':'',
        'purpose_codes':'00',
        'key_check_isChange':'5BDCB47BD3D8ECB9F3226FF7D6614A835A8735E5ED8EDEBA49E49D15',
        'leftTicketStr':'F%2FAJmwDx4QSPTfxEHgmaphlGo1MdX64auXkCXVHwkco6ULzOm1K%2B5CaQ1Js%3D',
        'train_location':'Q9',
        'choose_seats':'',
        'seatDetailType':'000',
        'roomType':'00',
        'dwAll':'N',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':'5ed1a56b8191cfcdc49e45eadbaa28f9',
    } # key_check_isChange 怎么来的？
      # a: 也是在initDc 获得的网页里 可以找到key_check_isChange 字段

    data = urllib.urlencode(data)

    res6 = urllib2.urlopen(req6, data=data)

    ret6 = res6.read()

    print ret6

def resultOrderForDcQueue():
    req7 = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue')
    req7.headers = headers
    data = {
        'orderSequence_no': 'E838900180',
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN':'5ed1a56b8191cfcdc49e45eadbaa28f9',
    } # orderSequence_no 是怎么填的？  这个应该是在confirm之后，queryOrderWaitTime请求后获得的。但是请求返回内容没有，是个bug？

    data = urllib.urlencode(data)

    res7 = urllib2.urlopen(req7, data=data)

    ret7 = res7.read()

    print ret7







