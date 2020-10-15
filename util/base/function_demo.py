# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/8/7

E-mail:keen2020@outlook.com

=================================


 """


# 递归 函数自己调用自己

def sum_numbers(num):
    print(num)
    # 递归出口很重要，否则出现死循环
    if num == 1:
        return
    # 调用自己
    sum_numbers(num - 1)


sum_numbers(3)
print('打印结束')







