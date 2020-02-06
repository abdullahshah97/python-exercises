name = input("Hello you are our guest, what is your name?\n")
print("Nice to meet you "+ name.title())
with open("guest.txt",'a') as file_object:
	file_object.write(name.title())

print("Hi there, please enter all the names in your party or then enter q:\n")
cont = True
with open("guest.txt","r+") as file_object:
	while cont:
		name = input("Enter a name: ")
		if name == "q":
			cont = False
		else:
			file_object.write(name.title())
	lines = file_object.readlines()
	for line in lines:
		print("\n We hope you enjoy your stay, "+line.strip())

