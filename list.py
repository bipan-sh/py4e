# I've commented everything because there are multiple exercises and
#They use same variable name as I spend more time on thinking variable
# name than writing program, hence no fancy names

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
#This is to list the words in each sentence and list the unique words
#book = open('romeo.txt')
#uniqueword = list()
#for line in book:
#    line = line.rstrip()
#    word = line.split()
#    alpha = sorted(word)
#    print(alpha)
#
#
#    for i in word:
#        if not i in uniqueword:
#            uniqueword.append(i)
#uniqueword = sorted(uniqueword)
#print(uniqueword)

# Exercise 5. minimalist email client

#thefile = open('short.txt')
#
##This loop will read thefile
#for line in thefile:
#    # only show lines starting with From
#    if line.startswith('From:'):
#        line = line.rstrip()
#        splitting = line.split()
#        print(splitting[1])

#Exercise 6: Rewrite the program that prompts the user for a list of
#numbers and prints out the maximum and minimum of the numbers at
#8.16. EXERCISES 107
#the end when the user enters “done”. Write the program to store the
#numbers the user enters in a list and use the max() and min() functions to
#compute the maximum and minimum numbers after the loop completes.

numlist = list()

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break

    try:
        number = int(number)

    except:
        print('Not a valid number')
    numlist.append(number)

print(numlist)
print(f"maximum number entered is: ", max(numlist))
print(f"minimul number entered is: ", min(numlist))

