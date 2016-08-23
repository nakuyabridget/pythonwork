#This is a string object

name = 'Nakuya'

if name.startswith('Nak'):
	print('Yes, the string starts with "Nak"')

if 'a' in name:
	print('yes, it contains the string "a"')

if name.find('aku') != -1:
	print('Yes, it contains the string "aku"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'Uganda', 'Rwanda']
print(delimiter.join(mylist))