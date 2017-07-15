# -*- coding:utf-8 -*-
'''
Created on 2017年7月10日

@author: Rookie
'''

#判断列表中有无重复值和重复值出现的个数
import random

list1 = list()
i = 0
while i < 10:
	x = random.randint(10, 15)  #构建一个随机的列表
	list1.append(x)
	i += 1
print list1

for x in list1:
	if list1.count(x) > 1:
		print x, list1.count(x)

#合并两个列表去除重复的值
list2 = [1, 3, 5, 7, 9]
list3 = [2, 3, 7, 8, 6]
list4 = list2 + list3
list5 = []

i = 0
for x in list4:
	if x not in list5:
		list5.append(x)

print list5