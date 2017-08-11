
name = raw_input ("name")
name = name.split(",")
for i in range(3):
	name[i] = name[i].strip(" ")
	name[i] = name[i].strip("[")
	name[i] = name[i].strip("]")
	name[i] = name[i].strip("'")

def upper_first(s):
	s = s.lower()
	lis = list(s)
	lis[0] = lis[0].upper()
	lis = "".join(lis)
	return lis
	

print map(upper_first,name)