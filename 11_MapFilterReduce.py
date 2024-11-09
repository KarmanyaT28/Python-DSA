from functools import reduce

# Sample list

numbers = [1,2,3,4,5]

# map: Doubles each number in the list

doubled = list(map(lambda x: x*2,numbers))
print(doubled)



evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)



total = reduce(lambda x,y: x+y,numbers)
print(total)
