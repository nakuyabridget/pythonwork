#Unpacking argument lists/tuples:
'''The reverse to arbitrary argument lists is that the reverse situation occurs 
when the arguments are already in a list or tuple but need to be unpacked for a function
call requiring seperate positional arguments. For instance, the built-in range() function
expects seperate start and stop arguments.If they are not available seperately, write
the function call with the * - operator to unpack the arguments out of a list or tuple:'''

list(range(1,10))#lists numbers from 1 upto the 2nd last number before 10...ie 1 to 9

args = [3,6]
list(range(*args))#outputs an array of numbbers from 1 upto the 2nd last number ie from 1 to 0

