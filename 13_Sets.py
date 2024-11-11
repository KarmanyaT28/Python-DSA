# Creating a set

unique_numbers = {1,2,3,4}


# Adding elements

unique_numbers.add(5)
print(unique_numbers)


# Removing elements

unique_numbers.remove(3)
print(unique_numbers)


# Checking membership
print(2 in unique_numbers)
print(3 in unique_numbers)


# Set operations: Union , Intersection, Difference


set_a = {1,2,3}
set_b = {3,4,5}

print(set_a | set_b)  # Union: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Intersection: {3}
print(set_a - set_b)  # Difference: {1, 2}
