# -*- coding: utf-8 -*-

class Parent(object):

	def override(self):
		print "Parent override()"
		
class Child(Parent):

	def override(self):
		print "Child, before parent override()"
		super(Child, self).override()
		print "Child, after parent override()"
	
dad = Parent()
son = Child()

dad.override()
son.override()