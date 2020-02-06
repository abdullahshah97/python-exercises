from random import randint

def comp_answer():
	"""Generate computer's choice via random generator"""
	num = randint(1,3)
	if num == 1:
		return 'r';
	elif num == 2:
		return 'p';
	elif num == 3:
		return 's';

def user_input(name):
	"""retrieve user input"""
	choice = input("Select a move " + name + ": r/p/s\n")
	return choice.lower()

def evaluate(comp, user):
	"""Decide if computer wins or user"""
	if comp == user:
		return -1 # Draw
	if 'r' == comp:
		if 's' == user:
			return 0 # Player loses
		else:
			return 1 # Player wins
	if 's' == comp:
		if 'p' == user:
			return 0
		else:
			return 1
	if 'p' == comp:
		if 'r' == user:
			return 0
		else:
			return 1
def intro():
	print("Hello! Let's play Rock, Paper, Scissors\n")
	name = input("What shall I call you?\n")
	print("Nice to meet you " + name + ", let' play!\nIf you want to quit just type 'q'")
	return name

def print_message(comp, user, result):
    message = "You chose " + user + ", the computer chose " + comp + "."
    if result == -1:
    	message += " It was a draw."
    if result:
    	message += " Congratulations you won!"
    else:
    	message += " You lost better luck next time!"
    print(message)

def game():
	user = ''
	name = intro()
	while ('q' != user):
		comp = comp_answer()
		user = user_input(name)
		if 'q' != user:
			result = evaluate(comp, user)
			print_message(comp, user, result)

game()