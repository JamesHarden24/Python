# -*- coding:utf-8 -*-
'''
Created on 2017年7月8日

@author: Administrator
'''

#求列表每个元素的3次方
def func_a(func_p, list1, n):
	i = 0
	while i < len(list1):
		list1[i] = func_p(list1[i], n)
		i += 1
	return list1

def func_b(m, n):
	return m ** n

li = [1, 3, 4, 5, 7]
li = func_a(func_b, li, 3)
print li
