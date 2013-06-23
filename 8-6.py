def count(word, letter):
	count = 0
	index = 0
	for letter in word:
		if word[index] == letter:
			count = count + 1
		index = index + 1
	print count

count('alelllllx', 'l')