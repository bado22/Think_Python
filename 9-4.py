def uses_only(word, string):
	for word_letter in word:
		if word_letter not in string:
			return False
	return True


print uses_only("Alex", "Az")