def nested_sum(integer_list):
	integer_list_sum = 0
	for i in integer_list:
		if isinstance(i, int):
			integer_list_sum += i
		elif isinstance(i, list):
			integer_list_sum += sum(i)
		else:
			pass
	return integer_list_sum

a = [1, 2, 3, [4, 5, 6]]

print nested_sum(a)