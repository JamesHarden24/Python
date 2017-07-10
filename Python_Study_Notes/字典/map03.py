# -*- coding:utf-8 -*-
'''
Created on 2017年7月8日

@author: Administrator
'''
import random

def func_min(a, b, c):
	if a < b:
		if a < c:
			return a
	else:
		if b < c:
			return b
	return c

#主执行函数
list1 = range(1000, 100000)
list2 = random.sample(list1, 10) #从list1中取出随机10个不重复的元素
list3 = random.sample(list1, 10)
list4 = random.sample(list1, 10)

print list2
print list3
print list4

list5 = map(func_min, list2, list3, list4)
print list5