#Aurhor : NAKUYA BRIDGET, a young software enginneer who is passionate about Python programming language

import random
number = random.randint(0,15)
upper_limit = int(input("Fizz buzz counting upto to:\n"))
start = True
while start:

	if number  %5 == 0 and number %3 == 0:
		print ("FizzBuzz")
	elif number  %3 == 0:
		print ("Fizz")

	elif number  %5 == 0:
		print ("Buzz")

	else:
		print (number)
		break
