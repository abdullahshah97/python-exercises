from random import seed
from random import randint


def starting_option():
    name = input("What is your name?\n")
    hard = input("Hello "+name+" try to guess my number between 1 and 20.\nDo you want limited tries (4)? (yes/no)\n")
    if "yes" == hard.lower() or "y" == hard.lower():
        hard = 1
    else:
        hard = 0
    options = {
    'player_name' : name,
    'difficulty' : hard
    }
    return options

def number_generator():
    """Generates random number for player to guess"""
    return randint(1, 20)

def run_game(hard, number):
    guess = ""
    count = 0
    while(number != guess and count < 4):
        if count > 3:
            return False
        guess = input("What do you think my number is?\n")
        guess = int(guess)
        if guess == number:
            return True
        elif guess > number:
            print("Guess lower!\n")
        elif guess < number:
            print("Guess higher!\n")
        if hard:
            count += 1

def result(winner, name):
    if winner:
        print("Congratulations " + name + "! You win!\n")
    else:
        print("Better luck next time " + name +".\n")


def game() :
    options = starting_option()
    number = number_generator()
    winner = run_game(options["difficulty"], number)
    result(winner, options['player_name'])

game()