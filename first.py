print("I'm now learning python from python for everyone\n")

def print_lyrics():
    print("Greenday")
    print("blink182")

print_lyrics()
age = input('Enter your dob ')

try:
    age_int = (2021 - int(age))
except:
    age_int = -1

if age_int > 0 and age_int < 130:
    print(f"Your age is {age_int}")


else:
    print('Not a valid number')

