# Write a short Python function, 
# is even(k), that takes an integer value and returns 
# True if k is even, and False otherwise.

def isEven(n):
	if n % 2 == 0:
		return True
	return False

result = isEven(12)
print(result)