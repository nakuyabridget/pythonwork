import random
number = random.randint(1,1000)
print("Let us play a guess game")

guess = int (input('What is the number?:'))
start = True
while start:
	if guess < number:
	    print("Too low")
	    guess = int (input('What is the number?:'))
	elif guess> number:
		print("Too high")
		guess = int (input('What is the number?:'))
	else:
		print ("Yay!! you got it!! {} is the number!".format (number));
		break
start=False
