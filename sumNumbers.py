import re

txt = open('regex_sum_317378.txt')
totle = 0
for line in txt:
	tmp = re.findall('[0-9]+',line)
	if len(tmp) == 0:continue
	i = 0
	while i < len(tmp):
		totle = totle + int(tmp[i])
		i = i + 1
	

print totle