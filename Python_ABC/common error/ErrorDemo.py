# Python新手入门学习常见错误

# 0
# project interpreter没有设定为python3


spam = 42

# 1
# 忘记在 if , elif , else , for , while , class ,def 声明末尾添加' ：'

# if spam == 42:
# 	print('Forget colon')

# SyntaxError ：invalid syntax


# 2
# 使用 = 而不是 ==
# = 是赋值操作符而 == 是等于比较操作。
#
# if spam == 42:
# 	print('Hello')
#
# while spam = 42:
# 	print('Hello')

# SyntaxError: invalid syntax


# 3
# 错误的使用缩进量

# print('Hello')
# print('Howdy')
# “IndentationError：unexpected indent”

# if spam == 42:
#     print('Hello!')
#     print('Howdy!')
# “IndentationError：unindent does not match any outer indentation level”

# if spam == 42:
# 	print('Hello!')
# print('Howdy!')
# IndentationError: unindent does not match any outer indentation level

# if spam == 42:
# print('Hello!')
# print('Howdy!')
# “IndentationError：expected an indented block”）

# 记住缩进增加只用在以'：'结束的语句之后，而之后必须恢复到之前的缩进格式。


# 4
# 在 for 循环语句中忘记调用 len()

# list1 = ['cat', 'dog', 'mouse']
# for i in range(len(list1)):
# 	print(list1[i])
# for item in list1:
# 	print(item)

# “TypeError: ‘list’ object cannot be interpreted as an integer”
# 通常你想要通过索引来迭代一个list或者string的元素，
# 需要调用range()函数时，记得返回len值而不是返回这个列表。


# 5
# 尝试修改string的值

# str = 'I have a pet cat.'
# str[13] = 'r'
# print(str)

# TypeError: ‘str’ object does not support item assignment
# string是一种不可变的数据类型


# 6
# 尝试连接非字符串值与字符串
# numEggs = 12
# print('I have ' + str(numEggs) + ' eggs.')
# print('I have ', numEggs, 'eggs.')

# TypeError: must be str, not int


# 7
# 在字符串首尾忘记加引号

# myName = 'Al'
# print('My name is ' + myName + .How are you?')
# SyntaxError: invalid syntax

# print('Hello')
# SyntaxError: EOL while scanning string literal


# 8
# 变量或者函数名拼写错误
#
# foobar = 'Al'
# print('My name is ' + foobar)
# NameError: name 'fooba' is not defined

# s = ruond(4.2)
# NameError: name 'ruond' is not defined

# s = round(4.2)
# NameError: name 'Round' is not defined


# 9
# 方法名拼写错误

# str = "Convert me to LOWERCASE"
# str = str.lower()
# print(str)
# AttributeError: 'str' object has no attribute 'lowerr'


# 10

# 引用超过list最大索引
# list2 = ['cat', 'dog', 'mouse']
# print(list2[2])
# IndexError: list index out of range


# 11
# 使用不存在的字典键值

# dict1 = {'cat':'Zophie', 'dog':'Basil', 'mouse':'Whiskers'}
# print('The name of my pet zebra is ' + dict1['zebra'])
# KeyError: 'zebra'


# 12
# 尝试使用Python关键字作为变量名

# class = 'algebra'
# SyntaxError: invalid syntax

# Python关键不能用作变量名
# Python3的关键字有：and, as, assert, break, class, continue, def,
# del, elif, else, except, False, finally, for, from, global, if,
# import, in, is, lambda, None, nonlocal, not, or, pass, raise,
# return, True, try, while, with, yield


# 13
# 在一个定义新变量中使用增值操作符
# eggs = 1
# eggs += 42
# # eggs = eggs + 42
# print(eggs)


# NameError: name 'eggs' is not defined


# 14
# 在定义局部变量前在函数中使用局部变量（此时有与局部变量同名的全局变量存在）

# someVar = 42
# def myFunction():
# 	print(someVar)
# 	# someVar = 100
# myFunction()

# UnboundLocalError: local variable 'someVar' referenced before assignment
# 在函数中使用局部变量那个而同时又存在同名全局变量时是很复杂的，
# 在函数中定义的变量，如果只在函数中使用那它就是局部的，反之就是全局变量。
# 这意味着你不能在定义它之前把它当全局变量在函数中使用。


# 15
# 尝试使用 range()创建整数列表
#
# s = list(range(10))
# s[4] = -1
# print(s)

# TypeError: 'range' object does not support item assignment
# 有时你想要得到一个有序的整数列表，所以 range() 看上去是生成此列表的不错方式。
# 然而，你需要记住 range() 返回的是 “range object”，而不是实际的 list 值。


# 16
# 不存在 ++ 或者 — 自增自减操作符
#
# m = 1
# m += 1
# SyntaxError: invalid syntax


# 17
# 忘记为方法的第一个参数添加self参数

# class Foo():
# 	def myMethod(self):
# 		print('Hello')
# a = Foo()
# a.myMethod()

# TypeError: myMethod() takes 0 positional arguments but 1 was given


# 18
# 中文字符

# print('爱睡懒觉的猫')


# SyntaxError: invalid character in identifier


# 19
# 函数形参与实参个数不符

# def addValue(x):
# 	sum = 0
# 	sum += x
# 	return sum
#
# x, y = 3, 4
# addValue(x)
# TypeError: addValue() takes 1 positional argument but 2 were given


# 20
# 该导入的模块没倒入进来

# import time
# print(time.time())
# NameError: name 'time' is not defined


# 21
# 调用模块内的函数不在前面加模块

# import math
# print(math.ceil(4.5))
# NameError: name 'ceil' is not defined
#
# import time
# print(time.time())
# TypeError: 'module' object is not callable
#
# from math import *
# print(ceil(4.5))
# 但是可能会出现模块之间的命名冲突问题，对代码的稳定性会有一定的影响


# 22
# 字典键值对象不是列表

# myCat = {'name':'Garfield','color':'orange','size':'fat'}
# print(myCat.keys()[0])
# TypeError: 'dict_keys' object does not support indexing

# python2可以，python3不可以


# 23
# 导入的模块没有提前安装

# import pyannote
# ModuleNotFoundError: No module named 'pyannote'


# 24
# 引用对象没有的属性

myCat = {'name':'Garfield','color':'orange','size':'fat'}
print(list(myCat.values()).order)
# AttributeError: 'list' object has no attribute 'order'



