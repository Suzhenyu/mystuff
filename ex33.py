# i = 0 
# numbers = []
# 
# while i < 6:
# 	print "At the top i is %d" % i
# 	numbers.append(i)
# 	
# 	i = i + 1
# 	print "Numbers now: ", numbers
# 	print "At the bottom i is %d" % i
# 	
# print "The numbers:"
# 
# for number in numbers:
# 	print number


# i = 0 
# numbers = []
# 
# def test_while(num, step):
# 	global i
# 	while i < num:	
# 		print "At the top i is %d" % i		
# 		numbers.append(i)
# 
# 		i = i + step		
# 		print "Numbers now: ", numbers		
# 		print "At the bottom i is %d" % i		
# 
# test_while(6, 2)
# 
# print "The numbers:"
# 
# for number in numbers:
# 	print number


i = 0 
numbers = []

def test_while(start, stop, step):
	for i in range(start, stop, step):
		print "At the top i is %d" % i		
		numbers.append(i)
		
		i = i + step		
		print "Numbers now: ", numbers		
		print "At the bottom i is %d" % i		

test_while(2, 6, 2)

print "The numbers:"

for number in numbers:
	print number