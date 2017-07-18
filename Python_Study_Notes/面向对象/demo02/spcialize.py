# -*- coding:utf-8 -*-

class Super:
	def method(self):
		print 'iN Super.method'

	def delegate(self):
		self.action()

	def action(self):
		assert 0,'action must be defined!'

class Inheritor(Super):
	pass

class Replace(Super):
	def method(self):
		print 'in Replace.method'

class Extender(Super):
	def method(self):
		print 'starting Extender.method'
		Super.method(self)
		print 'ending Extender.method'

class Provider(Super):
	def action(self):
		print 'in Provider.action'

if __name__ == '__main__':
	for klass in (Inheritor, Replace, Extender):
		print '\n' + klass.__name__ + '...'
		klass().method()
	print '\nProvider'
	x = Provider()
	x.delegate()