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

    """
    以下方法是继承 unittest.TestCase 这些方法有特殊的用途 通过改写这些方法 达到我们的目的
    setUpClass: 是类方法 必须使用装饰器 @classmethod 进行装饰 在整个测试类开始执行前执行
    setUp: 每天用例执行前会执行
    tearDown: 每天用例执行完成会执行
    tearDownClass: 是类方法 必须使用装饰器 @classmethod 进行装饰 在整个测试类执行结束后执行

    """

    # 拼接完整的excel路径，然后读取excel数据
    wb = ReadExcel(os.path.join(DATA_DIR, file_name), "login")
    cases = wb.read_column_data(read_column)

    @classmethod
    def setUpClass(cls) -> None:
        output_log.info("============================== 开始执行登录接口测试 ==============================")
        cls.request = HTTPRequest()

    def setUp(self):
        output_log.info('开始测试本条用例')

    def tearDown(self) -> None:
        output_log.info('该条用例执行完成')

    @classmethod
    def tearDownClass(cls) -> None:
        output_log.info("============================== 登录接口测试执行完毕 ==============================")
        cls.request.close()

    @data(*cases)  # 拆包，拆成几个参数
    def test_login(self, case):
        output_log.info('正在执行登录测试')

