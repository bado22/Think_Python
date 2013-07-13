import random

def sort_by_length(words):
	t = []
	for word in words:
		t.append((len(word), word))

	t.sort(reverse=True)

	res = []
	for length, word in t:
		res.append(word)
	return res

def sort_by_length_random(words):
	t = []
	for word in words:
		t.append((len(word), random.random(), word))	

	t.sort(reverse=True)

	res = []
	for length, _, word in t:
		res.append(word)
	return res

if __name__ == "__main__":
	words = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

	t = sort_by_length_random(words)
	for x in t: 
		print x