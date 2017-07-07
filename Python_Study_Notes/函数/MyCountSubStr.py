# -*- coding:utf-8 -*-
'''
Created on 2017年7月6日

@author: Administrator
'''

#统计strToCount中有多少个ch
def countSubCh(strToCount, ch):
	c = 0
	i = 0
	while i < len(strToCount):
		if strToCount[i] == ch:
			c += 1
		i += 1
	print c

#找字符串中的子串
def countSubStr(strToCount, subStr):
	count = 0
	i = 0
	while i < len(strToCount) - len(subStr) + 1:
		if strToCount[i:i + len(subStr)] == subStr:
			count += 1
		i += 1
	print count


s1 = "Hello Houston Rockets Hou Hou Hou"
cc = "o"
countSubCh(s1, cc)

subStr1 = "Hou"
countSubStr(s1, subStr1)