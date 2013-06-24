def avoids(word, forbidden_letters):
	for letter in word:
		if letter in forbidden_letters:
			return False
		return True

# print avoids("alex", "d")

user_forbidden_letters = raw_input("Enter the forbidden letters!\n")

count = 0
fin = open('words.txt')
for word in fin:
	if avoids(word, user_forbidden_letters):
		count += 1

print count

fin.close()