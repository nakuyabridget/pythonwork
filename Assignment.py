#Aurhor : NAKUYA BRIDGET, a young software enginneer who is passionate about Python programming language
while True:
	try:

		upper_limit = int(input("Fizz buzz counting upto to:\n"))
		lower_limit = int(input("Fizz buzz counting from:\n"))

		for number in range(lower_limit, upper_limit):
			if number  %5 == 0 and number %3 == 0:
				print ("FizzBuzz")
			elif number  %3 == 0:
				print ("Fizz")

			elif number  %5 == 0:
				print ("Buzz")

			else:
				print (number)

	except ValueError :
		print("Check again and enter integer")
