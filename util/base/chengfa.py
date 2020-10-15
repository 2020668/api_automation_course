# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2020/8/7

E-mail:keen2020@outlook.com

=================================


"""


for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(j, i, j * i), end="\t")
    print()




"""
hello
python
人生苦短，我用PYTHON
川建国大统领
Python自动化测试

"""



# 异常处理

# 错误类型
# print(a)
# print('a' + 1)


# 捕获异常
a = 1
b = 2
# 尝试执行
try:
    print(a + b)
# 捕获指定类型的错误
except NameError as e:
    print('变量名错误, 处理方案...')
# 捕获指定类型的错误
except TypeError as e:
    print('类型错误, 处理方案...')
# 执行成功 没有报错
else:
    print('没有发现错误...')
# 无论是否报错, 最后执行这条语句
finally:
    print('程序运行完成')



# 捕获异常 并主动抛出异常
# 尝试执行
try:
    print(a + b)
# 捕获指定类型的错误
except NameError as e:
    print('变量名错误, 处理方案...')
    raise e
# 执行成功 没有报错
else:
    print('没有发现错误...')
# 无论是否报错, 最后执行这条语句
finally:
    print('程序运行完成')




# 捕获异常 通用方式 可处理所有异常
try:
    print(a + b)
# 捕获指定类型的错误
except:
    print('程序出现了报错, 请及时处理...')
else:
    print('程序运行正常')
finally:
    print('程序运行完成')