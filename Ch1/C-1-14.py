# Write a short Python function that takes a sequence of integer 
# values and determines if there is a distinct pair of numbers in 
# the sequence whose product is odd.

def oddPair(data): 
	count = 0
	for i in range(len(data)):
		if data[i] % 2 == 1:
			count++
			if count == 2:
				return True
	return False 


