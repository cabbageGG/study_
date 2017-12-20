#-*- coding: utf-8 -*-

# author: li yangjin

import urllib3
from urllib.parse import urlencode
import certifi

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)
url = 'https://kyfw.12306.cn/otn/leftTicket/query'

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'

data = {
    "leftTicketDTO.train_date": "2017-12-20",
    "leftTicketDTO.from_station": "GZQ",
    "leftTicketDTO.to_station": "WHN",
    "purpose_codes": "ADULT"
}

headers = {
    'User-Agent': User_Agent,
}

post_data = urlencode(data)
print (type(post_data))
get_url = url + "?" + post_data
print(get_url)
response1 = http.request("POST", url=get_url, headers=headers)
response2 = http.request("GET", url=get_url, headers=headers)
response3 = http.request("GET", url=url,fields=data, headers=headers)
print (response1.status)
print (response1.data)
print (response2.status)
print (response2.data)
print (response3.status)
print (response3.data)





