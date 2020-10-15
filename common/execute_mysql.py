# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/2

E-mail:keen2020@outlook.com

=================================


"""

import pymysql
from common.config import conf
from common.logger import output_log


class ExecuteMysql(object):

    def __init__(self):

        # 连接数据库
        self.con = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", 'user'),
            password=conf.get("mysql", "password"),
            database=conf.get("mysql", "database"),
            charset="utf8")
        output_log.info('数据库连接成功, host --> {}, database --> {}'.format(conf.get("mysql", "host"),
                                                                       conf.get("mysql", "database")))
        # 创建游标
        self.cur = self.con.cursor()

    def find_one(self, sql):

        output_log.info('正在执行查询数据库, sql --> {}'.format(sql))
        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据，并返回查询结果
        self.con.commit()
        res = self.cur.fetchone()
        output_log.info('数据库查询成功, 查询结果 --> {}'.format(res))
        return res

    def find_many(self, sql, number):

        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据，并返回查询结果
        self.con.commit()
        return self.cur.fetchmany(number)

    def find_all(self, sql):

        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据，并返回查询结果
        self.con.commit()
        return self.cur.fetchall()

    def find_count(self, sql):
        count = self.cur.execute(sql)
        self.con.commit()
        return count

    def close(self):
        self.con.close()


if __name__ == '__main__':

    db = ExecuteMysql()
    sql = "SELECT mg_id FROM sp_manager WHERE mg_name='tester';"
    res = db.find_one(sql=sql)
    print(res)
    print(type(res))
    # id, role_id, create_time = db.find_one(sql=sql)
    # print(id, role_id, create_time)
    # print(type(id, role_id, create_time))

