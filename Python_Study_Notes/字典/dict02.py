# -*- coding:utf-8 -*-
'''
Created on 2017年7月9日

@author: Administrator
'''

#构造空列表
dict1 = {}
dict2 = dict()

print dict1, type(dict1) #{} <type 'dict'>
print dict2, type(dict2) #{} <type 'dict'>

'''
构造如下一个列表 {'a':97, 'b':98,...,'z':122}
'''
TempDict = {}
NumList = range(97, 123)
i = 0
while i < len(NumList):
	c = chr(NumList[i])
	TempDict[NumList[i]] = c
	i += 1

print TempDict

def dd(x, y):
	return {x:y}
alpha = map(chr, NumList)
list1 = map(dd, alpha, NumList)
#print dict1
dict1 = dict()
for x in list1:
	listKey = x.keys()
	listValue = x.values()
	dict1[listKey[0]] = listValue[0]
	#print listKey
print dict1
