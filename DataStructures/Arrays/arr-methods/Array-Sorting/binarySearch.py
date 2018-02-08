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
