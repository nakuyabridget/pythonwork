#Calculate the 4000'th fib3 number.

import random
number = random.randint(0,4000)

def numbers(a,b,c,i,n):
	a=0
	b=1


print("\nEnter n for how many times to generate series")
print("\nFIBONACCI SERIES\n")

for i in range (0,4000):
	c = a+b
	a = b
	b = c
	print('c')
