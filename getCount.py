import re

def getCount(inputStr):
    lst = re.findall('[aeiou]',inputStr)
    return len(lst)

instr = raw_input("a string:")
print getCount(instr)