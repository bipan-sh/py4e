#b = {'a':9, 'x':8, 'y':5, 'z': 100}
#
#for k,v in sorted(b.items()):
#    #print(k,v)
#    print(v,k)

fhandle = open('romeo.txt')
d = dict()

for lines in fhandle:
    words = lines.split()

    for word in words:
        word = word.lower()
        d[word] = d.get(word, 0) + 1

lst = list()

for k,v in list(d.items()):
    lst.append((v, k))

lst.sort(reverse=True)

for k,v in lst[:10]:
    print(k,v)

