import timeit

def fibonacci_old(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_old(n-1) + fibonacci_old(n-2)

def fibonacci_new(n):
	if n in known:
		return known[n]

	res = fibonacci_new(n-1)
	known[n] = res
	return res

print timeit.Timer('fibonacci_old(1000000)').timeit()
print timeit.Timer('fibonacci_new(1000000)').timeit()