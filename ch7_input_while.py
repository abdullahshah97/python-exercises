# Chapter 7 Ibput and While
message = input('Say hello: ')
if message == 'hello':
	print('hey good job buddy, you can say hello')
else:
	print('wow, that was such a simple instruction')

# Enter string to int
x = input('Enter your age: ')
x = int(x)
if x > 12 and x < 20:
	print("calm down, you're like 12")
elif x>21:
	print('granpa alert!')
else:
	print("you're not really are you")
# modulo function
x = input('give me a number: ')
if int(x) % 10 == 0:
	print('oh multiple of 10, how original')
else:
	print('slave')

#while loop
print('i like being annoying and repeating you so just tell me when to quit ;)')
keep_answering = True
while keep_answering:
	message = input('say something: ')
	if message == 'something':
		print('you think youre smart?')
	elif message == 'quit' or message == 'q':
		keep_answering = False
	else:
		print(message)

exit = ''
active = True
while exit != quit and active:
	exit = input('testing three different kinds of exits, condition, variable boolean, break: ')
	if exit == 'flag':
		active = False
	elif exit == 'break':
		break

