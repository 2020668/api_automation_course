# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/2

E-mail:keen2020@outlook.com

=================================


"""

from common.config import conf
import random
import time

from common.http_request import HTTPRequest


# 接收号段，然后随机生成8位0-9的数字，添加在号段后面，组合成为指定号段的随机号码

def rand_phone(segment):
    phone = str(segment)
    for i in range(8):
        phone_end = random.randint(0, 9)
        phone += str(phone_end)
    return phone


# 获取随机的用户名，由6位包括数字，大写，小写字母组成
def rand_name():
    name = ""
    for i in range(6):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))  # ASCII表示数字
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([num, letter, Letter]))
        name += s
    return name


# 生成随机的ip地址
def rand_ip():
    ip = '{}.{}.{}.{}'.format(random.randint(0, 255), random.randint(0, 255),
                              random.randint(0, 255), random.randint(0, 255))
    return ip


def get_token(request_data):
    request = HTTPRequest()
    url = conf.get("env", "url") + "/api/private/v1/login"

    response = request.request(method="post", url=url, data=request_data)
    token = response.json()['data']["token"]
    request.close()
    print("")
    print("登录请求参数--> {}".format(request_data))
    print("登录结果--> {}".format(response.json()))
    time.sleep(1)
    return token
