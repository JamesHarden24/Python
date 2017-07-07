# -*- coding:utf-8 -*-
'''
Created on 2017年7月6日

@author: Administrator
'''


def subFind(str1, sub):
	i = 0
	while i  < len(str1) - len(sub) + 1:
		if str1[i:i + len(sub)] == sub:
			print i, sub
		i += 1
