def print_max(x, y):
	'''prints the maximum of two numbers.
	The two values must be integers.'''
	#conver to integers, if possible
	x = int(x)
	y = int(y)

	if x > y:
		print(x, 'is maximum')

	else:
		print(y, 'is maximum')

	print_max(3,5)
	print(print_max.__doc__)

#Autor: Nakuya bridget, a young aspiring software engineer
#The return statement is used to return from a function i.e break out of the function.We can optionally return a value from the function as well.
#The output of this code 3 but when l try running it from the command prompt, it doesnt show any erros or even any indication that the file is not found or anything like that
#YET it doesnt show me any output still...this is not the first time this happenned, it has happennd for a couple of other times, dunno waht cd be wromg really!
