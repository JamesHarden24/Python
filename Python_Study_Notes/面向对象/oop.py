# -*- coding:utf-8 -*-

#class FirstClass
class FirstClass:
	def setData(self, value):
		self.data = value

	def display(self):
		print self.data

#class SecondClass
class SecondClass(FirstClass):
	def setName(self, str):
		self.name = str

	def getName(self):
		print self.name


x = FirstClass()
x.setData(5)
x.display()

x.NewData = '12345'
print x.NewData

y = SecondClass()
y.setName('Houston Rockets')
y.getName()


