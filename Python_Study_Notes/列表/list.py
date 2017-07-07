# -*- coding:utf-8 -*-
'''
Created on 2017年7月4日

@author: Administrator
'''

#列表 中可以保存不同的类型
li = [1, 2, 3, 4, 78]
print li

li[2] = '7'
print li

li[3] = [1, 2, 3, 4]

print li[3][3] #print 4


#列表中的for语句 迭代器 iterator
for inLi in li:
	print inLi,
	li.pop()  #删除尾部

#获取li列表中最大的值
li = [11, 5, 15, 9, 45]
print li
i = 0
max1 = li[0]
while i < len(li):
	if li[i] > max1:
		max1 = li[i]
	i += 1
print "max = " + str(max1)

#获取li中第二大的数字
if li[0] > li[1]:
	max1 = li[0]
	max2 = li[1]
else:
	max1 = li[1]
	max2 = li[0]

i = 2
while i < len(li):
	if max2 < li[i] <= max1:
		max2 = li[i]
	elif li[i] > max1:
		max2 = max1
		max1 = li[i]
	i += 1

print max1, max2

#获取li中第二大的数字 方法二
if li[0] > li[1]:
	max1 = li[0]
	max2 = li[1]
else:
	max1 = li[1]
	max2 = li[0]
for x in li:
	if max2 < x <= max1:
		max2 = x
	elif x > max1:
		max2 = max1
		max1 = x
print max1, max2 