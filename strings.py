#
#fruit = 'banana'
#count = 0
#
#for letter in fruit:
#    if letter == 'a':
#        count = count + 1
#        print(count)
#    else:
#        continue
#
#print('Total number of a is ', count)
#
#Exercise 5: Take the following Python code that stores a string:
#str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after the
#colon character and then use the float function to convert the extracted
#string into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'

a = str.find(':')
print(a)

b = str[a+1:]
print(b)
float_b = float(b)
print(float_b)

