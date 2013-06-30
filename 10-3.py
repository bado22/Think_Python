def sum_of_me_and_before(list):
	new_list = []
	total = 0
	for i in list:
		total += i
		new_list.append(total)
	return new_list

my_list = [1, 2, 3]
print sum_of_me_and_before(my_list)