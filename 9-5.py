def uses_all(word, string):
	for letter in string: 
		if letter not in word:
			return False
	return True

# print uses_all("ex", "Ale")

fin = open('words.txt')
count = 0
for word in fin:
	if uses_all(word, "aeiou") == True:
		count += 1

print "The words that use all the vowels aeiou are: ", count

count = 0
for word in fin:
	if uses_all(word, "aeiouy") == True:
		count += 1

print "The words that use all the vowels aeiouy are: ", count

fin.close()