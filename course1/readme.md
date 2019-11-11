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

# 字符串操作
```
len(s) 长度
isdecimal 只包含十进制字符
isalpha 只包含字母
isnumeric 只包含数字字符
isdigit 只包含数字
```

# 文件
```
open(filename,mode)打开文件
mode ： r 只读，文件不存在报错
        w 只写，覆盖写，文件不存在自动创建
        a 文件末尾追加
        r+ 读写
write() 写文件
writelines()将字符串写入文件
read 返回包含整个文件的字符串
readline 文件下一行内容
readlines 返回整个文件列表  换行符结尾
close 关闭文件
```

# OOP
```
class ClassName:
    def ___init__(self,...):
        pass

python是允许多继承
class ClassName(superClassName...):
    pass
```

# random [随机数](https://docs.python.org/3/library/random.html)
```
random() [0,1.0)浮点数
uniform(a,b) a和b之间的随机浮点数
randint(a,b) a和b之间的随机整数数,包含a,b
choice(<list>) 从列表中随机返回一个元素
shuffle(<list>) 将列表元素随机打乱
sample(<list>,k) 从指定列表随机获取k个元素
```

# enumerate
```
将可遍历的组合转为索引序列
for i,v in enumerate(list)
```

# zip 
```
zip([iterable, ...])
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
然后返回由这些元组组成的列表
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
利用 * 号操作符，可以将元组解压为列表。
```

# 数据可视化函数库[matplotlib模块](https://matplotlib.org/gallery.html)
```
matplotlib的子模块pyplot提供了2D图表制作的基本函数
import matplotlib,pyplot as plt
plt.scatter(x,y) # x，y为坐标的列表
plt.show()
```

# NumPy 科学计算库
```
1.强大的N维数组对象array
2.成熟的科学函数库
3.实用的线性代数、随机数生成函数等
操作对象是多维数组narray
narray.shape数组的维度
创建数组np.array(<list>),np.arrange()...
改变数组形状reshape
```