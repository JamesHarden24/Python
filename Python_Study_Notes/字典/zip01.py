# -*- coding:utf-8 -*-
'''
Created on 2017年7月9日

@author: Administrator
'''

def MyZip(x, y):
	return (x, y)


list1 = range(1, 11)
list2 = list("abcdefghij")

list3 = zip(list1, list2)
print list3

list4 = map(MyZip, list1, list2)
print list4