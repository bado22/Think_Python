def reverse_lookup(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise ValueError("This is a value error")

d = dict()
d["alex"] = "hey"

print "This should print alex: %s" % reverse_lookup(d, "hey")
#print "This should print a ValueError: %s" % reverse_lookup(d, "something else")