numbers =[1,2,3,4,5,6]


# List comprehension to get squares of even numbers

squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
print(squares_of_evens)


# List comprehension with a condition
incremented_odds = [x+1 for x in numbers if x % 2 !=0]
print(incremented_odds)
