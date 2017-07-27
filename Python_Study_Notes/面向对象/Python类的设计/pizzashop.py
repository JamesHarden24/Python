# -*- coding:utf-8 -*-

from employee import PizzaRobot, Server

class Customer:
	def __init__(self, name):
		self.name = name

	def order(self, server):
		print self.name, " order form ", server

