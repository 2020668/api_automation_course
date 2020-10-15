# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/2

E-mail:keen2020@outlook.com

=================================


"""

import requests
from requests.sessions import Session
from common.logger import output_log

"""
封装requests类，根据用例中的请求方法，来决定发起什么类型的请求。输出logging日志
"""


class HTTPRequest(object):
    """记录cookies信息给下一次请求使用"""

    def __init__(self):
        # 创建session对象
        self.session = Session()

    def request(self, method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):

        method = method.lower()
        if method == "post":
            # 判断是否使用json来传参（适用于接口项目有使用json传参）
            if json:
                output_log.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, json))
                return self.session.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                output_log.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, data))
                return self.session.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == "get":
            output_log.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, params))
            return self.session.get(url=url, params=params, headers=headers, cookies=cookies)
        elif method == 'put':
            output_log.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, data))
            return self.session.put(url=url, data=data, headers=headers, cookies=cookies)
        elif method == 'delete':
            output_log.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, data))
            return self.session.delete(url=url, headers=headers, cookies=cookies)

    def close(self):
        self.session.close()


class HTTPRequest2(object):
    """不记录cookies信息给下一次请求使用"""

    # @staticmethod
    def request(self, method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):

        method = method.lower()
        if method == "post":
            # 判断是否使用json来传参（适用于接口项目有使用json传参）
            if json:
                output_log.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, json))
                return requests.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                output_log.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, data))
                return requests.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == "get":
            output_log.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, params))
            return requests.get(url=url, params=params, headers=headers, cookies=cookies)


if __name__ == '__main__':

    # res = [{'username': 'admin', 'age': 31, 'address': '上海'},
    #        {'username': 'linken', 'age': 20, 'address': '北京'},
    #        {'username': 'aaaaaa', 'age': 25, 'address': '广州'},
    #        {'username': 'abbab', 'age': 26, 'address': '深圳'},
    #        {'username': 'tester', 'age': 22, 'address': '武汉'}
    #        ]
    #
    # for i in res:
    #     sorted(i)
    # print(res)

    request = HTTPRequest()

    # ================= 不带token的post请求 =================
    # url = 'http://127.0.0.1:8888/api/private/v1/login'
    # data = {'username': 'admin', 'password': '123456'}
    #
    # response = request.request(method='post', url=url, data=data)
    # res = response.json()
    # print(res)

    # ================= 带token的post请求 =================
    # 先登录获取token
    # url = 'http://127.0.0.1:8888/api/private/v1/login'
    # data = {'username': 'admin', 'password': '123456'}
    # response = request.request(method='post', url=url, data=data)
    # res = response.json()
    # token = res['data']['token']
    # # 再来发起post请求
    # url = 'http://127.0.0.1:8888/api/private/v1/users'
    # headers = {'Authorization': token}
    # data = {'username': 'aaaaaa123', 'password': '123456'}
    # response = request.request(method='post', url=url, data=data, headers=headers)
    # res = response.json()
    # print(res)

    # ================= 带token的put请求 =================
    # 先登录获取token
    # url = 'http://127.0.0.1:8888/api/private/v1/login'
    # data = {'username': 'admin', 'password': '123456'}
    # response = request.request(method='post', url=url, data=data)
    # res = response.json()
    # token = res['data']['token']
    # # 再来发起put请求
    # url = 'http://127.0.0.1:8888/api/private/v1/users/635/state/true'
    # headers = {'Authorization': token}
    # response = request.request(method='put', url=url, headers=headers)
    # res = response.json()
    # print(res)

    # ================= 带token的delete请求 =================
    # 先登录获取token
    url = 'http://127.0.0.1:8888/api/private/v1/login'
    data = {'username': 'admin', 'password': '123456'}
    response = request.request(method='post', url=url, data=data)
    res = response.json()
    token = res['data']['token']
    # 再来发起put请求
    url = 'http://127.0.0.1:8888/api/private/v1/users/635'
    headers = {'Authorization': token}
    response = request.request(method='delete', url=url, headers=headers)
    res = response.json()
    print(res)





