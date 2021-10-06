#numlist = list()
#while True :
#    inp = input('Enter a number: ')
#    if inp == 'done':
#        break
#
#    numlist.append(inp)
#    inp = float(inp)
#average = sum(numlist) / len(numlist)
#
#print(average)

#2 fhand = open('sample.txt')
#for line in fhand:
#    line = line.rstrip()
#    if not line.startswith('From '):
#        continue
#    print(line)
#    words = line.split()
#    print(words)
#    email = words[1]
#    host = email.split('@')
#    website = host[1]
#    print(website)

# Exercises

book = open('romeo.txt')
uniqueword = list()
for line in book:
    line = line.rstrip()
    word = line.split()
    alpha = sorted(word)
    print(alpha)


#    for i in word:
#        if not i in uniqueword:
#            uniqueword.append(i)
#uniqueword = sorted(uniqueword)
#print(uniqueword)