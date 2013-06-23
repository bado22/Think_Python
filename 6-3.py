def is_between(x, y, z):
	if x <= y <= z:
		return True
	else:
		return False

x = int(raw_input("What is x?\n"))
y = int(raw_input("What is y?\n"))
z = int(raw_input("What is z?\n"))

is_between(x, y, z)