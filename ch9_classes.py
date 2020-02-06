# Creating a dog class

class Dog():
	"""A simple attempt at a dog class"""
	def __init__(self, name, age):	#This is the constructor, taking arguments to instantiate object attributes
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting down"""
		print(self.name.title()+" is now sitting.")

	def roll(self):
		"""Simulate a dog rolling"""
		print(self.name.title()+" rolled over!")

my_dog = Dog('Gary', 14)
print("My dog's name is "+ my_dog.name.title()+".")
print("His age is "+str(my_dog.age)+".")
my_dog.roll()
my_dog.sit()

class Restaurant():
	"""An object class representing a Restraunt"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("Welcome to "+self.restaurant_name+" where we serve "+self.cuisine_type+".")

	def open_restaurant(self):
		print("Hi, we are open! Come inside.")

my_restaurant = Restaurant('KFC', 'chicken')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()