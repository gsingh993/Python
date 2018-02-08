#Recursion 
#Recursion is a technique by which a function makes one or more calls to itself during execution, or by which a 
#data structure relies upon smaller instances of the very same type of structure in its representation.


################ Example 1: Factorial ###################################

def factorial(n):
	if n ==0: # Note: Alway establish a base case first
		return 1
	else:
		return n * factorial(n-1)

result = factorial(5)
print(result)

################ Example 2: Binary Search ###################################
# for simplicity
data = []
for i in range(0,20):
	data.append(i)

def binary_search(data, target, low, high): 
	if low > high: 
		return False
	else:
	 	mid = (low + high) // 2
	 	if target == data[mid]:
	 		return True
	 	elif target < data[mid]:
	 		return binary_search(data, target, low, mid -1) #recur on the left part 
	 	else:
	 		return binary_search(data, target, mid + 1, high) # recur on the right part


result1 = binary_search(data, 17, 0, 20)
print(result1)


################ Example 3: Linear Sum ###################################
S = []
for i in range(0,10):
	S.append(i)

def linearSum(S, n): 
	if n == 0:
		return 0
	else:
		return linearSum(S, n-1) + S[n-1]

result3 = linearSum(S,len(S))
print(result3)


################ Example 4: Reverse Sequence ###################################

S1 = []
for i in range(0,15):
	S1.append(i)

def reverse(S, start,stop):
	if start < stop - 1:
		S[start],S[stop-1] = S[stop-1],S[start]
		reverse(S, start+1, stop-1)
		

################ Example 5: Binary Recursion Summ ###################################

def binarySum(S, start, stop):
	if start >= stop:
		return 0
	elif start = stop -1:
		return S[start]
	else:
		mid = (start + stop) // 2
		return binary_search(S, start, mid) + binarySum(S, mid, stop)

	

























