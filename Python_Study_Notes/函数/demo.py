# -*- coding:utf-8 -*-
'''
Created on 2017年7月8日

@author: Zhang Xiao
'''
def MyAdd(x, y = 10):
	return x + y

z = MyAdd(12)
print z  #22

z = MyAdd(12, 13)
print z  #25

z = MyAdd(x = 12, y = 13)
print z  #25

z = MyAdd(y = 13, x = 10)
print z  #23