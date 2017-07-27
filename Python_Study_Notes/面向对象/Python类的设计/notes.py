# -*- coding:utf-8 -*-

'''
继承:是基于Python中的属性查找
多态:在obj.method的方法中，method的意义取决取obj的类型
封装:

方法也是对象

'''

rec = {}
rec["name"] = "Mel"
rec["age"]  = 40
rec["job"]  = "player/singer"

class rec:pass

rec.name = "Mel"
rec.age  =  40
rec.job  = "trainer/writer"


class Person:
	def __init__(self, name, job):
		self.name = name
		self.job  = job

	def info(self):
		print self.name, self.job




