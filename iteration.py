
lowest_so_far = 25000
print('Before: ', lowest_so_far)

for i in [43, 23, 90, 22, 9, 39]:
    if i < lowest_so_far:
        lowest_so_far = i
   # print('lowest so far:', i)
print('After: ', lowest_so_far)

#Exercise

#Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.
sum = 0
count = 0

numbers = 0
b = 0
small = 3000

while numbers >= 0:
    a = input('Enter a number: ')
    if a == 'Done':
        break
    else:
        try:
            a = int(a)
            sum = sum + a
            count = count + 1
            continue
        except:
            print('Not a valid number')

print(sum, count, sum/count)


while b >= 0:
    x = input('Enter a number: ')
    if x == 'Done':
        break
    else:
        try:
            x = int(x)
            if x < small :
                small = x

        except:
            print('Not a valid number')

print('The smallest number is', small)

