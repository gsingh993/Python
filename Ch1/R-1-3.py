# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, 
#and returns the smallest and largest numbers, in the form of a tuple of length two.

def minAndMax(data):
	minimum = maximum = data[0]

	for val in data:
		if val < minimum:
			minimum = val
		if val > maximum:
			maximum = val
	return maximum,minimum


data = [12,32,15,78,61,38,17,9]

results = minAndMax(data)
print(results)
