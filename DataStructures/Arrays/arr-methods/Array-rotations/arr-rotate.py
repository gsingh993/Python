#Write a function that will return a rotated array 

################## Solution 1: using slicing ###################

arr = []
for i in range(0,5):
	arr.append(i)
print(arr)

revArr = arr[5:2:-1]
print(revArr)


######################## Sting rotate################################

str = 'test'
revStr = str[::-1]
print(revStr)



