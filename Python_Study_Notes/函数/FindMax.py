# -*- coding:utf-8 -*-
'''
Created on 2017年7月6日

@author: Administrator
'''

def FindMax(listForFind):
	i = 1
	maxNum = listForFind[i]
	while i < len(listForFind):
		if maxNum < listForFind[i]:
			maxNum = listForFind[i]
		i += 1
	
	print maxNum

#查找第二大的数字
def FindSecondMax(listForFind):
	MaxNum    = listForFind[0]
	SecondMax = listForFind[0]

	i = 1
	while i < len(listForFind):
		if listForFind[i] >= MaxNum:
			SecondMax = MaxNum
			MaxNum = listForFind[i]
		elif listForFind[i] > SecondMax:
			SecondMax = listForFind[i]
		i += 1

	print MaxNum, SecondMax

list1 = [1, 2, 56, 78, 34, 56, 789, 89, 145, 1089]
FindMax(list1)
FindSecondMax(list1)
