number = 23
running = True

while running:
	guess = int(input('Enter an integer : '))

	if guess == number:
		print('Congratutions, you guessed it')
		# this causes the while loop to stop

		running = False
	elif guess < number:
		print('No, its a little higher than that.')

	else :
		print('The while loop is over .')
		# Do anything else you want to do there

	print('Done')