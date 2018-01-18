# -*- coding:utf-8 -*-
import json
import requests
import hashlib
import time


def yd_api(yy_url,request_data):
    yy_response = requests.get(yy_url,params=request_data)
    print yy_response.json()['web'][0]['value'][0]

def MD5(str):
    m_str = hashlib.md5(str).hexdigest()
    return m_str

def main():
    api_url='http://openapi.youdao.com/api'
    salt_=  str(int(round(time.time() * 1000)))
    app_id = '2da62186083c5374'
    str_= '显示'
    app_k = '8djc4fM7Cqm2AbECKdcChmRxXMjo5108'
    aa_ = app_id + str_ + salt_ + app_k
    sign_ = MD5(aa_)
    from_ = 'zh-CHS'
    to_  = 'EN'
    request_data = {'q':str_, 'appKey':app_id, 'from':from_, 'to':to_, 'sign':sign_, 'salt':salt_}
    yd_api(api_url,request_data)



if __name__ == '__main__':
    main()