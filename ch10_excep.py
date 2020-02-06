print("Keep entering numbers to add or then enter q")
cont = ""
while cont != "q":
	num1 = input("Enter a number to add: ")
	num2 = input("Enter another number to add: ")
	if num1 != "no" and num2 != "no":
		try:
			num1 = int(num1)
			num2 = int(num2)
		except ValueError:
			print("You need to enter numbers")
		else:
			print(num1+num2)
	cont = input("Do you want to continue (q)? ")

with open("sherlock.txt") as file_object:
	contents = file_object.read()
	a = contents.lower().count('sherlock')
	print(a)

