def print_n(s, n):
	if n <= 0:	
		return
	print s
	print_n(s, n-1)

def do_n(fo, n):
	if n <= 0:
		return
	fo()
	do_n(fo, n-1)

do_n(print_n("Hello", 5), 5)