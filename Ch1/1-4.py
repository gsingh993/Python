#Control flow 

#if/elif structures

# # if 
# 	first condition: first body
# # elif
# 	 second condition: second body
# # elif
# 	 third condition: third body
# # else:
# # 	fourth body


# while loops 

# while condition:
#	function body 

#for loops 

# for element in iterable: 
#	body 

#functions 

# # def count(data, target): 
# 		n=0
# # 	for item in data:
# # 		if item == target:
# # 		n += 1 
# 		return n

points={ A+ :4.0, A :4.0, A- :3.67, B+ :3.33, B :3.0, B- :2.67, C+ :2.33, C :2.0,C :1.67, D+ :1.33, D :1.0, F :0.0}

def computeGPA(grades, points)

	num courses = 0 total points = 0 for g in grades:
		if g in points:
		num courses += 1
		total points += points[g]
    return total points / num courses