def pg79(x, y):
	x = y
	y = (x + a/x) / 2

def test_square_root(a):
	while True:
		print a, pg79, math.sqrt, abs(pg79 - math.sqrt)