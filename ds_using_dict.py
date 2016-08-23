#'ab' is short for 'a' ddress 'b' ook

ab = {
	'bridget': 'bnakuya@gmail.com',
	'isaac': 'iabook@gmail.com',
	'swabra': 'swabrakaterega@gmaul.com',
	'cidney': 'sidneyfeni@gmail.com'
	}

print("bridget's address is ", ab['bridget'])

#Deleting a key-value pair
del ab['cidney']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
	print('Contacts {} at {}'.format(name, address))

#Adding a key-value pair
ab['guido'] = 'guido@python.org'

if 'Guido' in ab:
	print("\nGuido's address is", ab['Guido'])
