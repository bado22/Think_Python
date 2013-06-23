"""
def split_names(full_name):
	full_name.split(' ')
	
	
name_input = raw_input("What is your name? (Just type your first and last name, please)\n")
split_names(name_input)
first_name = name_input[0]
last_name = name_input[1]

print "Your first name is %s and your last name is %s" % (first_name, last_name)
"""

s = "First Middle Last"
s.split(" ")