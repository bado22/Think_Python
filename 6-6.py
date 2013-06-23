def first(word):
	return word[0]

def last(word):
	return word[-1]
	
def middle(word):
	return word[1:-1]

def is_palindrome(word):
	n = len(word)
	if n % 2 == 0:
		return False
	elif last(word) == first(word):
		print word
	else: 
		return False

def ispalindrome(word):
    return word == word[::-1]
    
print ispalindrome("racecar")