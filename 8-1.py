def letters(s):
	index = 0
	while index < len(s):
		print s[index]
		index = index + 1

def backwards(s):
	index = len(s) - 1
	while index >= 0:
		print s[index]
		index = index - 1
		 
def anotherwayofletters(s):
	for char in s:
		print char

def separate_first_and_last_name(full_name):
	first_name = ''
	last_name = ''
	for letter in full_name:
		for letter in full_name:
			first_name = first_name + letter
			return first_name		
		print first_name

#print separate_first_and_last_name("Alex Baden")

def letter_count(letter, word):
	count = 0
	for char in word:
		if char == letter:
			count = count + 1
	print count

find('n', 'banana')