def is_power(a, b):
	if a/b == 0 and b**(a/b):
		return True
	else:
		return False
		
print is_power(2, 4)