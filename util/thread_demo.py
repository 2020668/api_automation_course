# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/7/27

E-mail:keen2020@outlook.com

=================================


"""

import time
import threading


def demo1():
    for i in range(2):
        print("正在加载中...")
        # 获取当前执行的线程
        print("当前活跃的线程有:{}".format(threading.current_thread()))
        time.sleep(1)


def demo2():
    for i in range(3):
        print("正在登录...")
        # 获取当前执行的线程
        print("当前活跃的线程有:{}".format(threading.current_thread()))
        time.sleep(1)


# 创建一个子线程执行demo1 并为线程设置name
t1 = threading.Thread(target=demo1, name="thread1")
# 创建一个子线程执行demo2 并为线程设置name
t2 = threading.Thread(target=demo2, name="thread2")

start_time = time.time()
# 执行子线程1
t1.start()
# 执行子线程2
t2.start()

# 获取线程的名称
print(t1.name)
print(t2.name)

# 获取当前执行的线程
print("当前活跃的线程有:{}".format(threading.current_thread()))

# 获取正在运行的所有线程
print("正在运行的所有线程:{}".format(threading.enumerate()))

# 获取正在运行的线程数量
print("正在运行的线程数量:{}".format(threading.active_count()))

# 等待子线程2执行完毕 再继续执行主线程 可传参数 等待子线程执行几秒后再执行主线程 这个时间不能大于子线程执行完毕所需的时间
# 可等待多个线程 耗时累计 一般不会设置时间
t2.join()
end_time = time.time()
print("程序运行耗时:{}".format(end_time - start_time))


