## Magicians, using functions for singular purposes
def show_magicians(magicians_list):
	for magician in magicians_list:
		print(magician)

def make_great(magicians_list):
	i = 0
	for magicians in magicians_list:
		magicians_list[i] = 'the great ' + magicians_list[i]
		i += 1
	return magicians_list

magicians = ['Rob','Chris','Ethan','Edith']
new_list = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_list)


#Sandwiches
def make_sandwiches(*toppings):
	print('making your sandwich with ')
	for topping in toppings:
		if toppings.index(topping) != len(toppings) - 1:
			print(topping,', ')
		else:
			print(topping)

make_sandwiches('a','b','c','v')
make_sandwiches('d','s')

def build_profile(first_name, last_name, **info): ##double asterix creates a dictionary
	user_profile = {}
	user_profile['first'] = first_name
	user_profile['last'] = last_name
	for k,v in info.items():
		user_profile[k] = v
	return user_profile

abdullah = build_profile('Abdullah', 'Shah', hobby = 'PlayStation', books = 'Harry Potter')
print(abdullah)
samya = build_profile('Samya', 'Shah', tv_show = 'Game of Thrones')
print(samya)
