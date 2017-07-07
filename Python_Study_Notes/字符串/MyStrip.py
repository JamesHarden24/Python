# -*- coding:utf-8 -*-
'''
Created on 2017年7月4日

@author: Administrator
'''
s0 = "@1243$%%www.rockets.com1234$5"
s1 = "@1243$%%5"

while s0[0] in s1:
	s0 = s0[1:]

while s0[len(s0)-1] in s1:
	s0 = s0[:len(s0)-1]

print s0
  