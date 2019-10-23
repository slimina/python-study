#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import keyword
import sys

print(sys.getdefaultencoding())

str = "你好"

# 单行注释

'''
多行注释
'''
"""
多行注释
"""
print(str.encode("gbk"))

print(str.encode("gbk").decode("gbk"))

print(keyword.kwlist)

a = 1
b = 2
c = 3

t = a + \
    b + \
    c
print(t)


if 2 > 1:
    print("true")
elif 1 == 1:
    print(" 11")
else:
    print("false")

tt = ["111", "222",
      "333", "444"]

print(tt)

# 同一行显示多条语句

x = 'runoob'; sys.stdout.write(x + '\n')