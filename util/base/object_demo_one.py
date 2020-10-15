# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/8/10

E-mail:keen2020@outlook.com

=================================


"""


class Person(object):

    def run(self):
        print('正在跑步...')

    # 方法 就是一个函数 在类里面叫方法
    def eat(self):
        print('正在吃饭')


lucy = Person()
print(lucy)

# 我们如果使用赋值语句 地址还是一样吗 ? 赋值只是修改的对象的引用 对象本身没有改变
lily = lucy
print(lily)





























