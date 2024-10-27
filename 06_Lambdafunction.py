# Lambda function to add two numbers

add = lambda x, y: x+y
print(add(5,3))


# Lambda function to square a number
square = lambda x: x*x
print(square(4))


# Using lambda in a map function to double each number in a list
numbers = [1,2,3,4]
doubled = list(map(lambda x: x*2 , numbers))
print(doubled)
