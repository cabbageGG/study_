#-*- coding: utf-8 -*-

# author: li yangjin

import requests

url = 'https://kyfw.12306.cn/otn/leftTicket/query'

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
params = {
    "leftTicketDTO.train_date": "2017-12-20",
    "leftTicketDTO.from_station": "GZQ",
    "leftTicketDTO.to_station": "WHN",
    "purpose_codes": "ADULT"
}

headers = {
    'User-Agent': User_Agent,
}

r = requests.get(url,params=params,headers=headers)

print (r.status_code)
print (r.content)
print (r.json())