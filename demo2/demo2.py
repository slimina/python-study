#!/usr/bin/env python3

# -*- coding: uft-8 -*-

str = 'sss ' \
      'ddd ' \
      'ddd'

aaa = '''
ssdsds
dsdsd
ds
'''

print(aaa)
print(str)

# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
str = r"this is a line with \n"
print(str)

str = "a" + "b"
print(str)

str = "abc" * 3
print(str)

# 字符串不能改变 没有单独的字符类型，一个字符就是长度为 1 的字符串
# 字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始

print("-------------------")
# 字面意义级联字符串
str = "abcdefghijklmn"
print(str)
print(str[-1])
print(str[0:-1])
print(str[2])
print(str[2:5])
print(str[2:])
