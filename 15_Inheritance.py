# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Another derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Creating instances
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Rex barks.
print(cat.speak())  # Output: Whiskers meows.



class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return f"{self.name} barks, and it's just {self.age} months old."

puppy = Puppy("Buddy", 6)
print(puppy.speak())  # Output: Buddy barks, and it's just 6 months old.


