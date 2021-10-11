#1  practice

#count = dict()
#names = ['gwen', 'lita', 'totti', 'guti', 'lita', 'ramos', 'totti']
#
#for name in names:
#    count[name] = count.get(name, 0) + 1
#
#print(count)

#2  counting the most occured word and its count
## open file
#fhandle = 'romeo.txt'
#book = open(fhandle)
#
#counts = dict()
#
### read the file line by line
#for lines in book:
#    lines = lines.rstrip()
#    words = lines.split()
#    print(words)
### the line above split the lines in words, and the loop will go through word by word and count it
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1
#print(counts)
#
#bigword = None
#bigcount = None
#
### this loop will go through the keys and value of dictionary counts
#for word, count in counts.items():
### the below condition will check each item and if the count is bigger that bigcount, replace the word and count in variables bigword and bigcount respectively
#    if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count
#
#print(bigword, bigcount)

#3 More counting words from a file and finding maximum and minimum value

# ask for input
#fhandle = input('Enter the filename: ')
## count length and if its less than 1 letter automatically open clown text
#if len(fhandle) < 1 :
#    filename = open('clown.txt')
#else :
#    filename = open(fhandle)
#
#di = dict()
#for line in filename:
#    #print(line)
#    words = line.split()
#    #print(words)
#    for word in words:
#        # idiom to count the words in the file
#        di[word] = di.get(word, 0) + 1
#
#print(di)
#
#max_word = None
#max_value = 0
#
#for k, v in di.items():
#    if v > max_value:
#        max_value = v
#        max_word = k
#print(max_word, max_value)

#Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines
#that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print
#out the contents of your dictionary (order does not matter).

#Sample Execution:
#python dow.py
#Enter a file name: mbox-short.txt
#{'Fri': 20, 'Thu': 6, 'Sat': 1}

#fhandle = open('short.txt')
#li = list()
#
#for lines in fhandle :
#    lines = lines.rstrip()
#    #condition to choose line that starts from ' From
#    if not lines.startswith('From') :
#        continue
#    line = lines.split()
#    # will skip the line starting with From which is less that 3 words in length
#    if len(line) < 3:
#        continue
#    #print(line[2])
#    # if 3rd word isn't there it'll add it, if it's there it'll add it too idk might have other proper way to do it that I don't know about
#    if line[2] not in li :
#        li.append(line[2])
#    else:
#        li.append(line[2])
#print(li)
#
#di = dict()
## using iteration and idion to count the word in the list
#for l in li:
#    di[l] = di.get(l, 0) + 1
#
#print(di)

#Exercise 3: Write a program to read through a mail log, build a his-togram using a dictionary to count how many messages have come from
#each email address, and print the dictionary.
# Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3, 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3, 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2, 'ray@media.berkeley.edu': 1}


fhandle = open('short.txt')
em = dict()
emails = list()

for line in fhandle :
    line = line.rstrip()
    #print(line)
    if not line.startswith('From '):
        continue
    words = line.split()

    if len(emails) >= 0:
        emails.append(words[1])

for email in emails:
    em[email] = em.get(email, 0) +1

print(em)

#Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary
#has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.

max_email = None
max_count = None

for k,v in em.items() :
    if max_count is None or v > max_count:
        max_count = v
        max_email = k

print(max_email, max_count)

#Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came
#from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
#python schoolcount.py
#Enter a file name: mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fhandle = open('short.txt')
emails = list()
web = list()
di = dict()

for line in fhandle :
    line = line.rstrip()
    #print(line)
    if not line.startswith('From '):
        continue
    words = line.split()
    #print(words[1])

    if len(emails) >= 0:
        emails.append(words[1])
#print(emails)

for email in emails:
    email = email.split('@')
    #print(email)
    web.append(email[1])

#print(web)

for w in web:
    di[w] = di.get(w, 0) + 1

print(di)
