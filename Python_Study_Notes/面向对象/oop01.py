# -*- coding:utf-8 -*-

#最小的Python类
class rec:pass

rec.name = 'Tracy'
rec.age = 40

print rec.name

print rec.__dict__.keys()

rec1 = rec()
rec2 = rec()

rec1.name = 'Houston'
print rec1.__dict__.keys()
print rec1.__class__
print rec.__bases__