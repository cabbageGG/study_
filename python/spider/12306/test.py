#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/10/24 上午10:05

__author__ = 'li yangjin'

import urllib, urllib2

import ssl, cookielib, json, re


ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

def login_init():
    print '>>>>>>>>>>>begin login_init'
    print 'login_initgin    cookie%s' % cj
    url = 'https://kyfw.12306.cn/otn/login/init'
    req = urllib2.Request(url)
    req.headers = headers
    res = opener.open(req)
    header_res = res.info()
    print 'login_initgin header_res: %s' % header_res
    if res.getcode() == 200:
        print 'login_init succ'
        # uamtk()
    else:
        print 'login_init fail code: %s' % res.getcode()

def getcode():
    print '>>>>>>>>>>>begin getcode'
    print 'getcode  cookie%s' % cj
    req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand')
    req.headers = headers
    response = opener.open(req)
    header_res = response.info()
    print 'getcode header_res: %s' % header_res
    file = response.read()
    with open('out.png', 'wb') as fn:
        fn.write(file)


def userLogin():
    print '>>>>>>>>>>>begin userLogin'
    print 'userLogin    cookie%s' % cj
    req = urllib2.Request('https://kyfw.12306.cn/otn/login/userLogin')
    req.headers = headers
    data = {
        '_json_att': '',
    }
    data = urllib.urlencode(data)
    response = opener.open(req, data=data)
    ret = response.read()
    header_res = response.info()
    #print 'userLogin ret: %s' % ret
    print 'userLogin header_res: %s' % header_res

def pass_userLogin():
    print '>>>>>>>>>>>begin pass_userLogin'
    print 'pass_userLogin    cookie%s' % cj
    req = urllib2.Request('https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin')
    req.headers = headers
    response = opener.open(req)
    ret = response.read()
    header_res = response.info()
    # print 'pass_userLogin ret: %s' % ret
    print 'pass_userLogin header_res: %s' % header_res

def uamtk():
    print '>>>begin uamtk'
    print 'uamtk    cookie%s' % cj
    req = urllib2.Request('https://kyfw.12306.cn/passport/web/auth/uamtk')
    req.headers = headers
    data = {
        'appid':'otn',
    }
    data = urllib.urlencode(data)
    response = opener.open(req, data=data)
    ret = response.read()
    header_res = response.info()
    print 'uamtk ret: %s' % ret
    print 'uamtk header_res: %s' % header_res
    retjson = json.loads(ret)
    global tk
    tk = retjson.get('newapptk','')
    print 'tk is : %s' % tk

def uamauthclient():
    print '>>>begin uamauthclient'
    print 'uamauthclient    cookie%s' % cj
    req = urllib2.Request('https://kyfw.12306.cn/otn/uamauthclient')
    req.headers = headers
    global tk
    data = {
        'tk': tk,  #关键点 tk参数怎么来的
    }
    data = urllib.urlencode(data)
    response = opener.open(req, data=data)
    ret = response.read()
    header_res = response.info()
    print 'uamauthclient ret: %s' % ret
    print 'uamauthclient header_res: %s' % header_res

def login():
    print '>>>>>>>>>>>begin'
    print 'begin cookie%s' % cj
    #login_init()
    #uamtk()
    getcode()
    print '请输入验证码：'
    code = raw_input()
    print '>>>>>>>>>>>begin check code'
    print 'check code cookie%s' % cj
    req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
    req.headers = headers
    data = {
        'answer': code,
        'login_site':'E',
        'rand':'sjrand',
    }
    data = urllib.urlencode(data)
    response = opener.open(req, data=data)
    #print response.read()  # 注意：这里response.read() 只能执行一次

    str1111 = response.read()

    header_res = response.info()
    print 'check code header_res: %s' % header_res

    result = json.loads(str1111)

    if result['result_code'] == '4':
        print '>>>>>>>>>>>begin login'
        print 'login    cookie%s' % cj
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
        header_res = res_login.info()
        print 'login header_res: %s' % header_res
        # userLogin()
        # pass_userLogin()
        uamtk()
        uamauthclient()
    else:
        print '验证码校验失败'
        login()


def queryTrain():
    print '>>>>>>>>>>>begin queryTrain'
    print 'queryTrain    cookie%s' % cj
    req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-02&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT')
    req.headers = headers
    req.add_header('If - Modified - Since', '0')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    response = opener.open(req)

    result = response.read()

    print type(result)

    res_json = json.loads(result)

    train_list = res_json['data']['result']

    print type(train_list)

    index = 0

    for i in train_list:
        t_list = i.split('|')
        # for t in t_list:
        #     print '[%s] %s' % (index, t)
        #     index += 1
        # break
        if t_list[28] == u'有':
            global Train_info
            Train_info = t_list
            return True
    return False


def checkUser():
    print '>>>>>>>>begin checkUser'
    print 'checkUser   cookie%s' % cj
    req1 = urllib2.Request('https://kyfw.12306.cn/otn/login/checkUser')
    req1.headers = headers
    res1 = opener.open(req1)

    ret1 = res1.read()
    headers_res = res1.info()
    print 'checkUser headers_res: %s' % headers_res

    print 'checkUser: %s' % ret1
    return ret1


def submitOrderRequest():
    print '>>>>>>>>begin submitOrderRequest'
    cj.set_cookie(make_cookie('_jc_save_fromStation', '%u957F%u6C99%2CCSQ'))
    cj.set_cookie(make_cookie('_jc_save_toStation', '%u6210%u90FD%2CCDW'))
    cj.set_cookie(make_cookie('_jc_save_fromDate', '2017-11-02'))
    cj.set_cookie(make_cookie('_jc_save_toDate', '2017-11-02'))
    cj.set_cookie(make_cookie('_jc_save_wfdc_flag', 'dc'))
    print 'submitOrderRequest    cookie%s' % cj
    req2 = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest')
    req2.headers = headers
    global Train_info
    if Train_info is None:
        print 'Train_info is None'
        return
    data = {
      'secretStr': Train_info[0],
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
    data = urllib.urlencode(data)
    print 'data: %s' % data
    res2 = opener.open(req2, data=data)

    headers_res = res2.info()
    print 'submitOrderRequest headers_res: %s' % headers_res

    ret2 = res2.read()

    print '提交订单返回结果: %s' % ret2

#getToken
def initDc():
    print '>>>>>>>>begin initDc'
    print 'initDc cookie%s' % cj
    req3 = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/initDc')
    req3.headers = headers
    req3.add_header('X-Requested-With', 'XMLHttpRequest')
    data = {
        '_json_att':'',
    }

    data = urllib.urlencode(data)

    res3 = opener.open(req3, data=data)

    headers_res = res3.info()
    print 'initDc headers_res: %s' % headers_res

    ret3 = res3.read()

    return ret3

#关键 有返回值 可选乘客信息
def getpassengerInfo():
    print '>>>>>>>>begin getpassengerInfo'
    print 'getpassengerInfo cookie%s' % cj
    req3 = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs')
    req3.headers = headers
    global token
    data = {
        '_json_att':'',
        'REPEAT_SUBMIT_TOKEN': token,
    } # REPEAT_SUBMIT_TOKEN 这个token 怎么得来的？
      # a: token 可以从前面初始化的页面initDc里拿到
      # 如： var globalRepeatSubmitToken = '35753d91155b9fdc35a4142018f3d6e3';

    data = urllib.urlencode(data)

    res3 = opener.open(req3, data=data)

    headers_res = res3.info()
    print 'getpassengerInfo headers_res: %s' % headers_res

    ret3 = res3.read()

    print 'getpassengerInfo return: %s' % ret3

def make_cookie(name, value):
    return cookielib.Cookie(
        version=0,
        name=name,
        value=value,
        port=None,
        port_specified=False,
        domain="kyfw.12306.cn",
        domain_specified=True,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=False,
        expires=None,
        discard=False,
        comment=None,
        comment_url=None,
        rest=None
    )

global Train_info
global html
global token
global tk

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)  # urlopne 默认使用 全局opener

if __name__ == '__main__':
    print 'cookie%s' % cj
    global Train_info
    Train_info = []
    login()
    if queryTrain():
        print "有票"
    else:
        print "无票"
    print Train_info
    # index = 0
    # for t in Train_info:
    #     print '[%s] %s' % (index, t)
    #     index += 1
    res = checkUser()
    res = json.loads(res)
    is_login = res['data']['flag']
    # print is_login, type(is_login)
    if res['data']['flag']:
        print '已登陆'
    else:
        print '未登陆'
        #login()
    submitOrderRequest()
    html = initDc()
    with open('initDc.html', 'w') as fn:
        fn.write(html)

    with open('initDc.html', 'r') as f:
        html = f.read()
    str_token = re.search('.+globalRepeatSubmitToken.+?;', html).group()
    print str_token
    tokenlist = re.split('\'', str_token)
    if len(tokenlist) > 1:
        print 'globalRepeatSubmitToken: %s' % tokenlist[1]
        global token
        token = tokenlist[1]
    else:
        print 'globalRepeatSubmitToken is None'
        global token
        token = ''

    res = getpassengerInfo()






