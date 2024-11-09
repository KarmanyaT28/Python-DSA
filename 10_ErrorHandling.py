# Basic error handling example

try:
	number = int("not a number")
except ValueError as e:
	print("Error occurred:",e)



# Handling multiple exceptions
try:
	result = 10 / 0

except ZeroDivisionError:
	print("Cannot divide by zero!")
except Exception as e:
	print("An error occurred:", e)
finally:
	print("Execution complete.")
