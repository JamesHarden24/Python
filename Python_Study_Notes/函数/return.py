# -*- coding:utf-8 -*-
'''
Created on 2017年7月8日

@author: Administrator
'''

def MyAdd(x, y):
	z = x + y
	return z

def MyMinus(x, y):
	return x - y

print MyAdd(10, 20)
print MyMinus(52, 89)

#返回多个参数
def MySwap(a, b):
	return a, b

x = 10
y = 11
x, y = MySwap(x, y)
print x, y