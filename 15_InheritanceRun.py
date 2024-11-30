class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return f"{self.name} barks, and it's just {self.age} months old."

puppy = Puppy("Buddy", 6)
print(puppy.speak())  # Output: Buddy barks, and it's just 6 months old.

