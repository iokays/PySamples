#!/usr/bin/python

# 1. Python 标识符
# 所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
# 单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
# 双下划线开头 __foo 代表类的私有成员
# 以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。


# 2. Python 可以同一行显示多条语句，方法是用分号 ; 分开

print('hello'); print('world')


# 3. 行和缩进: 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
# 建议在每个缩进层次使用 单个制表符 或 两个空格 或 四个空格 , 切记不能混用

if True:
    print('True')
else:
    print('False')


# 4. 多行语句: Python语句中一般以新行作为语句的结束符。
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示

one = 1
two = 2
three = 3

total = one + \
        two + \
        three

print(total)

# 5. Python 引号
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须是相同类型的。
#
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# 6. Python注释: Python中单行注释以 # 开头.
# python 中多行注释使用三个单引号 ''' 或三个双引号 """。

print("Hello Python!")  # 第一个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 7. Python空行: 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。
"""
类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。
"""

# 8. 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')


# 9. print 输出: print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

x = 'a'
y = 'b'

print(x, end='')
print(y, end='')

# 10. 多个语句构成代码组
"""
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
"""









