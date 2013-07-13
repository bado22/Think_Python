def sed(ps, rs, file1, file2):
	file1contents = open(file1, 'r')
	open(file2, 'w')
	print file1contents.read()

sed('alex', 'baden', 'words.txt', 'file2.txt')