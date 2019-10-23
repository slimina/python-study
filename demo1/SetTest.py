student = {'aaa','bbb','ccc','ddd','bbb'}

print(student)

if 'ccc' in student:
    print("ok")
else:
    print("fail")


a = set("a12b3")
b = set("abc")

print(a-b)  # a 和 b 的差集

print(a|b)  # a 和 b 的并集

print(a&b)  # a 和 b 的交集

print(a^b)  # a 和 b 中不同时存在的元素
