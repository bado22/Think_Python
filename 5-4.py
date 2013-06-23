def is_triangle(a, b, c):
	a = int(a)
	b = int(b)
	c = int(c)
	
	if a + b < c or a + c < b or b + c < a:
		print "No"
	else:
		print "Yes"
		
a = int(raw_input("What is the length of the first side?"))
b = int(raw_input("What is the length of the second side?"))
c = int(raw_input("What is the length of the third side?"))

is_triangle(a, b, c)