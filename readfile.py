
#print(fhand)
#
#for cheese in fhand:
#    print(cheese)
#
#print(len(cheese)
a = input('Enter a file name: ')
fhand = open(a)

#inp = fhand.read()
#
#finder = inp.find('X-DSPAM-Confidence: 0.8475')
#finder = int(finder)
#colon_finder = inp.find('0.8475')
#slicer = inp[finder:]

#for line in fhand :
#    line = line.rstrip()
#    if line.startswith('X-DSPAM-Confidence: 0.8475'):
#        #finder = line.find()
#        x = len(line)
#        print(x)
#        y = line.find(':')
#        slicer = line[20:]
#        print(slicer)
#

for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        break
    print(line)

#abc = inp.split()

#print(len(abc))