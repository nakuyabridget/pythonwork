upper_limit=int(input("enter the upper limit"))
lower_limit=int(input('enter lower limit'))

for number in range(lower_limit,upper_limit):
	if number %5==0 and number % 3 == 0:
		print "Fizz Buzz"
	elif number % 3 ==0:
		print"Fizz"
	elif number % 5==0:
		print "Buzz"
	else:
		print number


