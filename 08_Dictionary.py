# Creating a dictionary
profile = {
    "name": "Karmanya",
    "age": 24,
    "profession": "Information Security Analyst"
}

# Accessing values
print(profile["name"])  # Output: Karmanya

# Adding or updating key-value pairs
profile["location"] = "Noida"
print(profile)  # Output: {'name': 'Karmanya', 'age': 24, 'profession': 'Information Security Analyst', 'location': 'Noida'}

# Removing key-value pairs
del profile["age"]
print(profile)  # Output: {'name': 'Karmanya', 'profession': 'Information Security Analyst', 'location': 'Noida'}

# Getting all keys and values
print(profile.keys())    # Output: dict_keys(['name', 'profession', 'location'])
print(profile.values())  # Output: dict_values(['Karmanya', 'Information Security Analyst', 'Noida'])

# Checking if a key exists
print("profession" in profile)  # Output: True

