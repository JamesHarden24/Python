# -*- coding:utf-8 -*-
import FirstMod

class SecondClass(FirstMod.FirstClass):
	def setName(self, Name):
		self.Name = Name

	def setData(self, Data):
		self.Data = Data + 10

	def printData(self):
		print self.Data

x = SecondClass()
x.setData(20)
x.printData()


class ThirdClass(SecondClass):
	def __init__(self, value):
		self.Data = value

	def __add__(self, other):
		return ThirdClass(self.Data + other)
th1 = ThirdClass(60)
th2 = ThirdClass(80)
th3 = th1 + th2
print th3.Data