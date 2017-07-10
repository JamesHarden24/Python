# -*- coding:utf-8 -*-
'''
Created on 2017年7月9日

@author: Administrator
'''
s = "abcdef"
#    012345
print s[2], s[3:5]

li = range(1, 11)
print li, li[2:5]

t = (2, 3, 4, 5)

#s[1] = "B" 只读有序不允许不允许被修改
#t[1] = 30  只读有序不允许不允许被修改
li[2] = 30
print li

#字典 key可以是任何类型
d = {1:'a', 1.5:1, 'b':3.3, "hello":"Houston"}
print d

# dict[key]
print d[1]
print d[1.5]
print d['b']
print d["hello"]