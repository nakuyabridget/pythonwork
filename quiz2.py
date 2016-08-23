
walking = True
distance=102
leicester_to_london=0
london_to_Leicester=102
miles_covered=0

while miles_covered !=distance:
	if leicester_to_london!=london_to_Leicester:
	leicester_to_london+=2
	london_to_Leicester-=1
else:
	print london_to_Leicester
	walking =False
