#Examples of mutable objects are lists, dictionaries or instances of classes
def f(a, L=[]):
	L.append(a)
	return L
print (f(1))
print (f(2))
print (f(3))