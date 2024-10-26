# Defining a function in Python

def greet(name):
	return f"Hello, {name}!"



# Calling the function

print(greet("Karmanya"))


# Function with default arguments

def add(a, b=5):
	return a+b

print(add(10))
print(add(10,20))
