def capitalize_all(t):
	res = []
	for s in t: 
		res.append(s.capitalize())
	return res

def capitalize_nested(l):
	list_letters = []
	for i in list_letters:
		if isinstance(i, int):
			integer_list_sum += i
		elif isinstance(i, list):
			integer_list_sum += sum(i)
		else:
			pass
	return integer_list_sum