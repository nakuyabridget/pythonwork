def parrot(voltage, state='a stiff', action='voom'):
	print("--This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.", end=' ')
	print("E's", state, "!")

d = {"voltage": "four million", "state": "bleeding' demised", "action": "VOOM"}
parrot(**d)