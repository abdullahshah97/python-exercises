###Chapter 10 files and exceptions###

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

#read line by line
file_name = "pi_digits.txt"
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())

with open(file_name) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

#Storing the file object as a list of lines - allowing us to work on it woutside of with block
pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)

#Is your birthday in pi?
birthday = input("Enter your birthdate ddmmyy: ")
if birthday in pi_string:
	print("Your birthday is in the first million digits of pi!!")
else:
	print("Your birthdate is NOT in the first million digits of pi :(.")