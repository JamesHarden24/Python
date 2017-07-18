# -*- coding:utf-8 -*-

class NextClass:
	def printer(self, text):
		self.message = text
		print self.message

class Super:
	def __init__(self, x):
		self.name = x

class Sub(Super):
	def __init__(self, x, y):
		Super.__init__(self, x)
		self.name2 = y

I = Sub(1, 2)
print I.name, I.name2
