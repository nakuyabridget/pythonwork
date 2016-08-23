def parrot (voltage, state='a stiff', action='voom',type='Norwegian Blue'):
	print ("--This parrot wouldn't", action , end=' ')
	print ("if you put", voltage, "volts through it.")
	print ("--Lovely plumage, the",type)
	print ("--it's", state, "!")

parrot (1000)											#1 positional arguement
parrot (voltage=1000)									#1 keyword argument
parrot (voltage=1000000, action='VOOOOOOM')				#2 keyword arguments
parrot (action='VOOOOOO', voltage=1000000)				#2 keyword arguments
parrot ('a million', 'berefit of life', 'jump')			#3 positional argumets
parrot ('a thousand', state='pushing up the daisies' )  #1 positional, 1 keyword

#But the following calls would be invalid
#parrot() 						required argument missing
#parrot(voltage=5.0,'dead')		non-keyword arguement after a keyword argument
#parrot(110, voltage=220)		duplicate value for the same argument
#parrot(actor='John Cleese')	unknown keyword argument