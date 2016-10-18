def find_it(seq):
    dic = dict()
    for i in seq:
        dic[i] = dic.get(i,0) + 1
    for a in dic:
        if dic[a] % 2 == 1:
            return a


que = raw_input("some squence:")
print find_it(que)