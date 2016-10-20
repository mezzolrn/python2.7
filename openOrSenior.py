def openOrSenior(data):
	lst = list()
	for i in data:
		if i[0] >= 55 and i[1] > 7:
			lst.append("Senior")
		else:
			lst.append("Open")
	return lst

data = raw_input("Data:")
data = eval(data)
print openOrSenior(data)
