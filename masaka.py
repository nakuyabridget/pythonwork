walking_to_masaka = 0
walking_to_Kamapala=102

walking = True

while walking:
	if walking_to_masaka < walking_to_Kamapala:
		print("Still walking at {}".format(walking_to_masaka))
		print("Still walking at {}".format(walking_to_Kamapala))

		walking_to_masaka += 2
		walking_to_Kamapala -= 1
	else:
		walking = False

		print("They meet at{}".format(walking_to_masaka))
		
