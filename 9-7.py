def has_three_consecutive_double_letters(word):
	i = 0
	count = 0
	while i < len(word) - 1:
		if word[i+1] == word[i]:
			count += 1
			if count == 3:
				return True
			i = i + 2
		else:
			count = 0
			i = i + 1
	return False


def check_for_has_three_consecutive_double_letters(fin):
	fin = open(fin)
	for word in fin:
		word = word.strip() 
		if has_three_consecutive_double_letters(word) == True:
			print word
	fin.close()

check_for_has_three_consecutive_double_letters('words.txt')

