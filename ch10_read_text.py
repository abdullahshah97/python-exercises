with open("ch10_text.txt") as file_object:
	lines = file_object.readlines()
	for x in range(0,3):
		for line in lines:
			print(line.strip())

file_object1 = open("ch10_text.txt")
lines = file_object1.readlines()
text_together = ''
for line in lines:
	text_together += line.replace('Python','Java').rstrip()
print(text_together)