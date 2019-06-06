# -*- coding:utf-8 -*-

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):

 	def __init__(self, name):
 		## Dog has-a name
 		self.name = name

## Cat is-a Animal
class Cat(Animal):
	
	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Person is-a Animal
class Person(Animal):
	
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		# Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		## ?? hmmm what is this strange magic?
		super(Employee, self).__init__(name)
		
		## Employee has-a property: salary
		self.salary = salary

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan


		
		