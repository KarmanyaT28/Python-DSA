# Defining a class

class Person:
	def __init__(self, name , age):
		self.name = name
		self.age = age


	def greet(self):
		return f"Hello, my name is {self.name} and i am {self.age} years old."


# Creating an object (instance of the class)

person1 = Person("Karmanya", 24)

print(person1.greet())


# Modifying attributes

person1.age = 25
print(person1.greet())
