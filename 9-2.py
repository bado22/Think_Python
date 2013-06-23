def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True

def avoids(word, forbidden):
	for letter in word:
		if letter in forbidden:
			return False
	return True
	
def print_words_without_e(fin):
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if has_no_e(word):
			print word
	return True		

print_words_without_e()