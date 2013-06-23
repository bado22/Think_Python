def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print "Holy smokes, Fermat was wrong!"
	else:
		print "No, that doesn't work"
		
a = int(raw_input("What is a?\n"))
b = int(raw_input("What is b?\n"))		
c = int(raw_input("What is c?\n"))
n = int(raw_input("What is n?\n"))
		
check_fermat(a,b,c,n)