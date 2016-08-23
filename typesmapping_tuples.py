"""When a final parameter of the form **name is present, it recieves a dictionary(see typesmapping) 
containing all keyword arguments except for those corresponding to a formal parameter.
This may be combined with a formal parameter of the form *name wchich recives a tuple containing
 the positional arguments beyond the formal parameter list. (*name must occur before **name.) For example 
 we define a function like this:"""


def cheeseshop(kind, *arguments, **keywords):
	print("--Do you have any", kind, "?")
	print("-- l'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 40)
	keys = sorted(keywords.keys())
	for kw in keys:
		print(kw, ":", keywords[kw])

cheeseshop("Limburger","It's very runny, sir.",
			"it's really very, VERY runny, sir.",
			shopkeeper="Nakuya Bridget",
			client="Namayanja Swabra",
			sketch="Cheese Shop Sketch")

"""Note that the list of keyword names is created by sorting
the result of the keyword's dictionary's keys() method before
printing it's contents;if this is not done, the order in
wchich the arguments are printed is undefined"""