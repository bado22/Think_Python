def split_names(full_name):
	return full_name.split()

	
name_input = raw_input("What is your name? (Just type your first and last name, please)\n")
#print "The name_input is", name_input
name_list = split_names(name_input)
#print "The name_list is", name_list
first_name = name_list[0]
last_name = name_list[1]

print "Your first name is %s and your last name is %s" % (first_name, last_name)