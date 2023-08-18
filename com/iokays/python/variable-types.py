#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 变量赋值

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
print(a, b, c)

a, b, c = 1, 2, "john"
print(a, b, c)

var1 = 1
var2 = 2
print(var1, var2)

del var1
print(var2)

# Python支持四种不同的数值类型：
"""
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）

长整型也可以使用小写 l，但是还是建议您使用大写 L，避免与数字 1 混淆。Python使用 L 来显示长整型。
Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。
long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。
"""

# Python字符串
"""
python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
"""

s = "abcdef"
print(s[1:5])

# 当使用以冒号分隔的字符串，python 返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。
# 上面的结果包含了 s[1] 的值 b，而取到的最大范围不包括尾下标，就是 s[5] 的值 f。

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）

print(s[1:4:2])

# Python 列表

# 列表用 [ ] 标识，是 python 最通用的复合数据类型。
# 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
h = ['h', 'i', 'j', 'k', 'l', 'm', 'n']

print(a)
print(a[1:5])
print(a[1:5:2])
print(a * 2)
print(a + h)

# Python 元组
# 元组是另一个数据类型，类似于 List（列表）。
# 元组用 () 标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表。

tuple2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

print(tuple2)
print(tuple2[1:5])
print(tuple2[1:5:2])
print(tuple2 * 2)
print(tuple2 + tuple2)

# Python 字典
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
# 字典的关键字必须为不可变类型，且不能重复。

dict2 = {}
dict2['one'] = "This is one"
dict2[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict2['one'])
print(dict2[2])
print(tinydict)
print(dict2.keys())
print(tinydict.keys())
print(tinydict.values())

# Python数据类型转换
# 数据类型的转换，你只需要将数据类型作为函数名即可。

print(int('1'))
print(float('1.1'))
print(str(1.1))
print(tuple(a))
print(list(tuple2))
print(ord('a'))
print(hex(1))

