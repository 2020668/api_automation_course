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
from common.tools import get_token, rand_name
from common.execute_mysql import ExecuteMysql

# 从配置文件获取数据
file_name = conf.get('excel', 'file_name')
read_column = conf.get('excel', 'read_column')
read_column = eval(read_column)  # 将str转换成list


@ddt
class AddUserTestCase(unittest.TestCase):
    # 拼接完整的excel路径，然后读取excel数据
    wb = ReadExcel(os.path.join(DATA_DIR, file_name), "add_user")
    cases = wb.read_column_data(read_column)

    @classmethod
    def setUpClass(cls) -> None:
        output_log.info("============================== 开始执行新增用户接口测试 ==============================")
        cls.request = HTTPRequest()
        cls.db = ExecuteMysql()

    @classmethod
    def tearDownClass(cls) -> None:
        output_log.info("============================== 新增用户接口测试执行完毕 ==============================")
        cls.request.close()

    @data(*cases)  # 拆包，拆成几个参数
    def test_add_user(self, case):

        # 拼接url地址
        url = conf.get("env", "url") + case.url
        # 行数等于用例编号+1
        self.row = case.case_id + 1

        # 获取token
        token = get_token(eval(case.token_data))

        # 拼接headers
        headers = {'Authorization': token}

        # 由于是注册接口 注册使用的用户名每次需要更改 所以使用参数化 使用随机名称来替换
        username = rand_name()
        case.request_data = case.request_data.replace('#username', username)

        # 向接口发送请求
        response = self.request.request(method=case.method, url=url, headers=headers, data=eval(case.request_data))
        time.sleep(2)

        # 该打印的内容会显示在报告中
        print("")
        print("请求地址--> {}".format(url))
        print("请求参数--> {}".format(case.request_data))
        print("期望的返回结果--> {}".format(case.expected_data))
        print("服务器响应数据--> {}".format(response.json()))

        res = response.json()

        if '创建成功' in str(res):
            sql = 'SELECT mg_id, role_id, mg_time FROM sp_manager WHERE mg_name="{}"'.format(username)
            mg_id, role_id, create_time = self.db.find_one(sql=sql)
            expected_data = {
                'data': {'id': mg_id, 'username': username, 'role_id': role_id, 'create_time': create_time},
                'meta': {'msg': '创建成功', 'status': 201}}

        try:
            self.assertEqual(expected_data, res)
        except AssertionError as e:
            result = 'FAIL'
            output_log.exception(e)  # 将异常信息记录到日志
            raise e
        else:
            result = 'PASS'
            output_log.info("预期结果:{}, 实际结果:{}, 断言结果:{}".format(expected_data, res, result))
        finally:
            # 向Excel回写服务器返回结果
            self.wb.write_data(row=self.row, column=10, value=str(response.json()))
            # 向Excel回写断言结果
            self.wb.write_data(row=self.row, column=11, value=result)

            # 由于excel用例的期望结果 也采用了参数化 为了直观查看 在测试完成后 将期望结果的具体值回写到excel
            self.wb.write_data(row=self.row, column=9, value=str(expected_data))
