
#Quiz 2
#Use a while loop to solve the following problem:
#A slow, but determined, walker sets off from 
#Leicester to cover the 102 miles to London at 2 miles per hour. 
#Another walker sets off from London heading to Leicester going at 1 mile per hour. Where do they meet?

Leister = 0
london= 102

walking = True
while walking:
	if Leister < london:
		print("Still walking at {}".format(Leister))
		print("Still walking at {}".format(london))

		Leister += 2
		london -= 1
	else:
		walking = False

		print("They meet at{}".format(london))
		
