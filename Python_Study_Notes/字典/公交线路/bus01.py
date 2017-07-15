# -*- coding:utf-8 -*-
'''
Created on 2017年7月10日

@author: Rookie
'''
str1 = "aa bb cc dd ee ff gg hh"
str2 = "bb bbx csc dcd eee eff ff egg rhh"
str3 = "aaa bbc cec bb dd ee ff ggg fhh"

#公交1的字典
str_list = str1.split()
num_list = range(0, len(str_list))
tuple_list = zip(num_list, str_list)
dict1 = dict(tuple_list)
dict1_keys = dict1.keys()

#公交2的字典
str_list = str2.split()
num_list = range(0, len(str_list))
tuple_list = zip(num_list, str_list)
dict2 = dict(tuple_list)
dict2_keys = dict2.keys()

#公交3的字典
str_list = str3.split()
num_list = range(0, len(str_list))
tuple_list = zip(num_list, str_list)
dict3 = dict(tuple_list)
dict3_keys = dict3.keys()

dict_list = []
dict_list.append(dict1)
dict_list.append(dict2)
dict_list.append(dict3)

start_name = "bb"
end_name   = "ff"

#找到直达线路
for dict_temp in dict_list:
	for k in dict_temp.keys():
		if dict_temp[k] == start_name:
			start = k
		if dict_temp[k] == end_name:
			end = k
	
	for x in dict_temp.values()[start:end]:
		print x, "->",
	print dict_temp.values()[end]
		