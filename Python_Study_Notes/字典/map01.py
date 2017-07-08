# -*- coding:utf-8 -*-
'''
Created on 2017年7月8日

@author: Administrator
'''

def mul(func, list1, list2):
	i = 0
	list_return = []
	while i < len(list1):
		list_return.append(func(list1[i], list2[i]))
		i += 1
	return list_return

def func_a(a, b):
	return a * b

lt = range(5, 10)
lw = range(8, 13)

li = []
li = mul(func_a, lt, lw)
print li

def p_2(x):
	return x * x

li = map(p_2, li)
print li
