class Animal:
	def speak(self):
		return "Some generic sound."

class Dog(Animal):
	def speak(self):
		return "Bark."

class Cat(Animal):
	def speak(self):
		return "Meow."


# Polymorphic behavior

animals = [Dog(),Cat(),Animal()]


for animal in animals:
	print(animal.speak())


print(len("Karmanya"))
print(len([1,2,3,4]))
