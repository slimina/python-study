#!/usr/bin/env python3

# -*- coding: uft-8 -*-

a = 1
b = 2

a,b = b,a
print(a,b)

a = ["hello" ,"world","!"]

print(" ".join(a))

# 列表中频率最高的值

a = [2,4,3,2,3,45,1,7,8,90,1,3,5,2,2,1]
print(max(set(a),key = a.count))

from collections import Counter
cnt = Counter(a)
print(cnt.most_common(6))

str1 = "hello"
str2 = "olleh"
print(Counter(str1) == Counter(str2))


str1 = " hello world !"
print(str1[::-1])

print(reversed(str1))
for char in reversed(str1):
    print(char)

mun = 123456789
print(int(str(mun)[::-1]))

aa = [2,3,4,5,6,7]
print(aa[::-1])

aa =[['a','b'],['c','d'],['e','f']]
tran = zip(*aa)
print(list(tran))

b = 6
print( 1<b<9)
print(6 == b < 10)

def product(a,b):
    return a *b

def add(a,b):
    return a+b

b = True
print((product if b else add)(2,3))