filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("yes")
else:
    print("no")
print(pi_string[:52] + '...')
print(len(pi_string))

