def square_root(a):
	while True:
		epsilon = .0000000000001
		y = (x + a/x) / 2
		if abs(y - x) < epsilon:
			break
		x = y

square_root(16)