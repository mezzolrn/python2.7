num = raw_input("num:")
num = num.split(",")
print num

for i in range(len(num)):
	num[i] = int(num[i])


def time(a,b):
	return a * b

print reduce(time,num)