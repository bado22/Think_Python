def compare(x, y):
	if x > y:
		return 1
	elif x == y:
		return 0
	elif x < y:
		return -1
		
x = int(raw_input("What is x?\n"))
y = int(raw_input("What is y?\n"))

a_number = compare(x, y)

print "That means the statement returns %r" % a_number