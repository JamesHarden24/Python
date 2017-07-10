# -*- coding:utf-8 -*-
'''
Created on 2017年7月8日

@author: Administrator
'''

def func_x(x):
	return 2 * x + 3

lx = range(3, 9)
ly = map(func_x, lx)
print ly

lt = zip(lx, ly)
print lt

i = 3
while i < 9:
	print ly[lx.index(i)]
	i += 1