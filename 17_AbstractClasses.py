from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass  # Must be implemented in child classes

class Dog(Animal):
    def speak(self):
        return "Bark."

class Cat(Animal):
    def speak(self):
        return "Meow."

# Attempting to instantiate an abstract class will result in an error
# animal = Animal()  # TypeError: Can't instantiate abstract class

# Correct usage
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Bark.
print(cat.speak())  # Output: Meow.

