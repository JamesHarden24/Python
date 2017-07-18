# -*- coding:utf-8 -*-
'''
运算符重载
运算符重载让类拦截常规的Python运算
类可以重载所有Python表达式运算符
类可重载打印、函数调用、属性点号运算符运算
重载使类实例的行为像内置类型
重载使通过提供特殊名称的类方法来实现的

常见的运算符重载的方法：
__init__     构造器方法
__del__      析构方法
__add__      运算符 +
__or__       运算符 | （位or）
__repr__, __str__ 打印，转换
__call__     函数调用
__getattr__  点号运算
__setattr__  属性赋值语句
__getitem__  索引运算
__setitem__  索引赋值语句
__len__      长度
__cmp__      比较 ==
__lt__       特定比较  小于比较
__eq__       特定比较  判断相等
__radd__     左侧加法
__iadd__     实地增强加法
__iter__     迭代环境
'''

class Number:
	def __init__(self, start):
		self.data = start

	def __sub__(self, other):
		return Number(self.data - other)

x = Number(5)
y = x - 2
print y.data


class indexer:
	def __getitem__(self, index):
		return index ** 2

x = indexer()
print x[2]


