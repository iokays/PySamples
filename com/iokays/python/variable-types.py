#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 变量赋值

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

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




















