# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/8/11

E-mail:keen2020@outlook.com

=================================


"""



# 多态 不同的子类对象 调用相同的父类方法 产生不同的执行结果
# 可以增加代码的灵活度 以继承和重写父类方法为前提
class Animal(object):

    def __init__(self, name):

        self.name = name

    # 公有方法
    def eat(self):
        print('{} 正在吃饭'.format(self.name))


class Cat(Animal):

    pass



Garfield = Cat('加菲猫')
Doraemon = Cat('多啦A梦')

Garfield.eat()
Doraemon.eat()



















