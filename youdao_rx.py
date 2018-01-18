# -*- coding:utf-8 -*-
#Author: rxg
import requests
import hashlib
import time


class Translate(object):

    def __init__(self, yy_url, yy_salt, yy_id, yy_keyt, yy_str, yy_from='auto', yy_to='auto'):
        self.yy_url = yy_url       # 请求API
        self.yy_salt = yy_salt     # 请求参数中的随机数（这里是当前时间的时间戳）
        self.yy_id = yy_id         # 应用ID
        self.yy_keyt = yy_keyt       # 应用密钥
        self.yy_str = yy_str       # 需要翻译的文本
        self.yy_from = yy_from     # 被翻译的文本语言
        self.yy_to = yy_to         # 翻译后文本的语言

    def md5(self):
        sign_ = self.yy_id + self.yy_str + self.yy_salt + self.yy_keyt    # 即将要加密的串
        m_sign = hashlib.md5(sign_).hexdigest()
        return m_sign

    def yy_api(self):
        m_sign = self.md5()
        params = {'q':self.yy_str, 'appKey':self.yy_id, 'from':self.yy_from, 'to':self.yy_to, 'sign':m_sign, 'salt':self.yy_salt}
        yy_response  = requests.get(self.yy_url,params=params)
        try:
            print yy_response.json()['web'][0]['value'][0]
        except KeyError:
            print 'sorry not found This word'



if __name__ == '__main__':
    url = 'http://openapi.youdao.com/api'    #  有道的公共API
    salt= str(int(round(time.time() * 1000)))   # 参数（随机数）
    id = '2da62186083c5374'   # 应用ID
    str_tr = '调用'   # 需要翻译的文字
    keyt = '8djc4fM7Cqm2AbECKdcChmRxXMjo5108'   # 应用密钥
    from_ = 'zh-CHS'
    to_ = 'EN'
    translate = Translate(url,salt,id,keyt,str_tr,from_,to_)
    translate.yy_api()