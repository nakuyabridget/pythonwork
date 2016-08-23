
#Author: Nakuya Bridget, a young software enginner who is passionate about the python programming language.
def fib(n):
	"""Print a Fibonacci series up to n."""

	a, b = 0, 1
	while a < n:
		print (a)
		a, b = b, a + b
	print()

#Now call the function we just defined:
fib(4000)

