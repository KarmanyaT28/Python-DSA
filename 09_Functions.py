# Defining a function that accepts another function as a parameter
def greet_user(func,name):
	return func(name)


# Callback function

def welcome(name):
	return f"Welcome, {name}!"


# Using the callback

print(greet_user(welcome, "Karmanya"))


# Lambda as a callback

print(greet_user(lambda name: f"Hello, {name}!", "Karmanya"))



