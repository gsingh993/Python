#Write a short Python function that takes a positive integer n and 
#returns the sum of the squares of all the odd positive integers smaller than n.

def sumOfOddSquares(n):
	total = 0
	for i in range(1,n+1,2):
		total+= i*i
	return total 


result = sumOfOddSquares(6)
print(result)