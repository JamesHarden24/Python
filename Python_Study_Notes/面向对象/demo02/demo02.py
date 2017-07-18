# -*- coding:utf-8 -*-

class ShareData:
	spam = 42

x = ShareData()
y = ShareData()

print x.spam, y.spam

ShareData.spam = 99

print x.spam, y.spam, ShareData.spam

x.spam = 88

print x.spam, y.spam, ShareData.spam

class MixedName:
	data = 'spam'
	def __init__(self, value):
		self.data = value

	def display(self):
		print self.data, MixedName.data

x = MixedName(1)
y = MixedName(3)
x.display()
y.display()