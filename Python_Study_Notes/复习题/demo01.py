# -*- coding:utf-8 -*-
'''
Created on 2017年7月10日

@author: Rookie
'''

#列表中有多少个"aa"
def count_sub(str_tmp, str_sub):
	i = 0
	count = 0
	while i < len(str_tmp) - len(str_sub):
		if str_tmp[i:i+len(str_sub)] == str_sub:
			count += 1
		i += 1
	return count

#列表中"aa"出现位置
def find_substr_index(str_tmp, str_sub):
	if len(str_tmp) < len(str_sub):
		return -1
	
	i = 0
	while i < len(str_tmp) - len(str_sub):
		if str_tmp[i:i+len(str_sub)] == str_sub:
			return i
		i += 1
	return -1

str1 = " aa bb vv ff rr dc aa gb bb aa rm"
sub = "aa"

print count_sub(str1, sub)
print find_substr_index(str1, sub)