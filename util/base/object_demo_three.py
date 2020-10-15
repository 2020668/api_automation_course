# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/8/11

E-mail:keen2020@outlook.com

=================================


"""


# 优先级 实例方法 类方法 静态方法
class Animal(object):

    # 类属性
    title = 'animal'

    def __init__(self):
        # 实例属性
        self.age = 5

    # 既不访问类属性/实例属性 也不调用类方法/实例方法 那么可以定义成静态方法
    # 静态方法 需要使用装饰器 @staticmethod 来标识  就跟我们定义的函数一样的 需要参数就传 不需要就不传
    # 减少不必要的内存占用和性能消耗
    @staticmethod
    def drink():
        print('这是静态方法...')

    # 实例方法
    def eat(self):
        print(self.age)
        print('这是实例方法...')

        # 实例方法内部可以调用静态方法
        self.drink()

    @classmethod
    def run(cls):
        print(cls.title)
        print('这是类方法')

        # 类方法内部也可以调用静态方法
        cls.drink()


Doraemon = Animal()
Doraemon.drink()
Doraemon.eat()
Doraemon.run()



# 区分应用场景

# 在方法内需要访问实例属性 或调用实例方法 就定义成实例方法

# 在方法内只需要访问类属性 或 调用类方法 就定义成类方法

# 在方法内既不访问类属性/实例属性 也不调用类方法/实例方法 为了减少内存占用和性能的消耗 就应当定义成静态方法































