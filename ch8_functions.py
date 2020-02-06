#Functions in Python

# Defining function, later calling it
def display_message():
	"""This is my first function in python"""
	print('hello, how are you?')

display_message()

def favourite_book(title):
	print('I see you like the book '+title.title())
favourite_book('Harry Potter')

def test_keywords( person, animal = 'bear', location = 'woods'):
	print('the ' + animal + ' ate ' + person + ' at ' + location)

test_keywords('jack', location = 'home')

def make_shirt(size = 'large', text = 'I love Python'):
	print('making a ' + size + ' shirt with the text "' + text.title() + '"')

make_shirt() #should print with default values
make_shirt('medium')
make_shirt('small','hello world!')

# Album, demonstrating how you can call
albums = []
artist = input('enter artists name: ')
title = input('title of their album: ')
def make_album(artist_name, title, tracks = ''):
	if tracks:
		album={'artist' : artist_name, 'title' : title, 'tracks' : tracks}
	else:
		album={'artist' : artist_name, 'title' : title}
	return album

albums.append(make_album('Eminem', 'Recovery', 3))
albums.append(make_album(artist, title))
for album in albums:
	for k, v in album.items():
		print(str(k) + ' ' + str(v))

