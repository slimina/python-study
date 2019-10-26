# math
```
pi
ceil(x) 对x向上取整
floor(x)
pow(x,y)
sqrt(x)
fsum(list) 集合元素求和
```
# 列表 list
```
append(x)
sort()
reverse()
index(x) 第一个出现x的位置
insert(i,x)
count(x) 元素x的个数
remove(x)
pop(i) 去除i位置元素，并删除
```
# datetime
```
datetime.now()
datetime.strptime()
datetime.strftime()
isocalendar 返回年  周数  周几
```
# 元组 tuple
```
特殊的序列，一旦创建不能被修改，表示 : (1,2,3)
访问和list相同
应用场景：固定数据项，函数多返回值
创建一个元素元组 :(1,)
元组通常用于不同类型，而列表用于相同类型
元组表示的是结构，列表则是顺序
```

# 集合 set
```
包含0个或多个数据项的无序组合
元素不重复
set()函数用于生成集合
通常表示成员关系，元素去重
s - t 或 s.difference(t) 返回集合s 不在集合t中
s & t 或 s.intersection(t) 同时在s,t集合中
s | t 或 s.union(t) s和 t 所有元素
s ^ t 或 s.symmetric_difference(t)  不同时在集合s和 t中元素
```

# 字典 dict
```
key:value  map
d[key] = value 增加
d[key] 访问
del d[key] 删除
key in d key是否在字典中
for key in d.keys(): 遍历key
for value in d.values(): 遍历value
for item in d.items(): 遍历项
```