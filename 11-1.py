import pprint

dictionary = dict()
fin = open('words.txt')
line = fin.readlines()
def engdicdefine():
    for word in line:
    	dictionary[word] = "hey"
    return dictionary

pprint.pprint(engdicdefine())