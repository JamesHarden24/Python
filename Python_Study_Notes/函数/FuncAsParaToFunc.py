# -*- coding:utf-8 -*-
'''
Created on 2017年7月8日

@author: Zhang Xiao
'''

#将函数名作为另外一个函数的形参
def func_s(func_f):
	func_f()

def func_f():
	print "func f"

func_s(func_f)

def func_a(func_p, t):
	i = 0
	while i < len(t):
		t[i] = func_p(t[i])
		i += 1
	return t

def func_b(x):
	return x + 5

li = [1, 3, 4, 5, 6]
li= func_a(func_b, li)
print li
