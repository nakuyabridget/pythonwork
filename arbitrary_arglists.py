'''finally,the least used option is to specify that a fraction can
be called with an arbitrary number of arguments.These 
arguments will be wrapped up in a tuple.Before the variable
number of arguments,zero or more normal arguments may occur:'''

def concat(*args, sep="/"):
	return sep.join(args)

	
concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")