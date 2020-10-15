# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/3

E-mail:keen2020@outlook.com

=================================


"""

import unittest
import os
import time

from library.ddt import ddt, data
from common.read_excel import ReadExcel
from common.logger import output_log  # 可直接导入对象
from common.config import conf
from common.constant import DATA_DIR
from common.http_request import HTTPRequest
from common.tools import get_token, get_sign
from common.execute_mysql import ExecuteMysql

# 从配置文件获取数据
file_name = conf.get('excel', 'file_name')
read_column = conf.get('excel', 'read_column')
read_column = eval(read_column)  # 将str转换成list

@ddt
class LoginTestCase(unittest.TestCase):

    # 拼接完整的excel路径，然后读取excel数据
    wb = ReadExcel(os.path.join(DATA_DIR, file_name), "login")
    cases = wb.read_column_data(read_column)

    @classmethod
    def setUpClass(cls) -> None:
        output_log.info("============================== 开始执行登录接口测试 ==============================")
        cls.request = HTTPRequest()

    @classmethod
    def tearDownClass(cls) -> None:
        output_log.info("============================== 登录接口测试执行完毕 ==============================")
        cls.request.close()

    @data(*cases)  # 拆包，拆成几个参数
    def test_login(self, case):

        # 拼接url地址
        url = conf.get("env", "url") + case.url
        # 行数等于用例编号+1
        self.row = case.case_id + 1
        # 向接口发送请求
        response = self.request.request(method=case.method, url=url, data=eval(case.request_data))
        time.sleep(2)

        # 该打印的内容会显示在报告中
        print("")
        print("请求地址--> {}".format(url))
        print("请求参数--> {}".format(case.request_data))
        print("期望结果--> {}".format(case.expected_data))
        print("服务器响应数据--> {}".format(response.json()))

        res = response.json()

        if "登录成功" in str(res):
            res = {'data': {'id': res['data']['id'], 'rid': res['data']['rid'], 'username': res['data']['username'], 'mobile': res['data']['mobile'], 'email': res['data']['email']}, 'meta': res['meta']}
            output_log.info('处理后的服务器返回数据 --> {}'.format(res))

        try:
            self.assertEqual(eval(case.expected_data), res)
        except AssertionError as e:
            result = 'FAIL'
            output_log.exception(e)  # 将异常信息记录到日志
            raise e
        else:
            result = 'PASS'
            output_log.info("预期结果:{}, 实际结果:{}, 断言结果:{}".format(case.expected_data, res, result))
        finally:
            # 向Excel回写服务器返回结果
            self.wb.write_data(row=self.row, column=9, value=str(response.json()))
            # 向Excel回写断言结果
            self.wb.write_data(row=self.row, column=10, value=result)
