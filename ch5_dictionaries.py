# Dictionaries
person = {'first_name' : 'Abdullah', 'last_name' : 'Shah', 'age' : 21, 'city' : 'London'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Useful way to define dictionaries when the keys are disjointed, kind of. Helps readability.
favourite_numbers = {
	'abdullah' : 7,
	'matt' : 100,
	'kacey' : 24,
	'lucas' : 50,
	'jeremy' : 2
}
# 2 ways to make strings, helps readability? "Neatily formatted" second one is
print("Kacey's favourite number is " + str(favourite_numbers['kacey']) + ".")

print("Abdullah's favourite number is " + 
	str(favourite_numbers['abdullah']) +
	"."
	"\nMatt's favourite number is " +
	str(favourite_numbers['matt']) +
	".")

# More concisely, loop through key and values
for key, value in favourite_numbers.items():
	print( 
		key.title() +
		"'s favourite number is " +
		str(value) +
		".")

rivers = {
	'nile' : 'Egypt',
	'thames' : 'England',
	'amazon river' : 'South America'
}

for key, value in rivers.items():
	print( "The " +
	key.title() +
	" runs through the country " +
	value.title() +
	".")

# Can use .keys() but it is default, unless its needed to be explicitly mentioned for readability
for key in rivers:
	print(key.title())

for value in rivers.values():
	print(value)

# Using lists and dictionaries
favourite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
}

poll_names = ['MATT','luCaS','SARAh','pHil','jane']
poll_names_lower = [names.lower() for names in poll_names] #sanitising user input
for name in poll_names_lower:
	if name.lower() in favourite_languages:
		print('Thanks for taking the poll, '+ name.title())
	else:
		print('Please take the poll, ' + name.title())



#6-7
person1 = {'first_name' : 'Abdullah', 'last_name' : 'Shah', 'age' : 21, 'city' : 'London'}
person2 = {'first_name' : 'Susan', 'last_name' : 'Ward', 'age' : 46, 'city' : 'New York'}
person3 = {'first_name' : 'Joey', 'last_name' : 'Tribbiani', 'age' : 61, 'city' : 'Brooklyn'}
persons = []
persons.append(person1)
persons.append(person2)
persons.append(person3)

for person in persons:
    for k,v in person.items():
        print(k.title()+" : "+str(v))


# 6-8
jack = {'species':'Cat','owner':'Abdullah'}
jill = {'species':'Dog','owner':'April'}
judy = {'species':'Fox','owner':'Max'}
janice = {'species':'Rabbit','owner':'Umar'}

pets = [jack,jill,judy,janice]
for pet in pets:
	for k,v in pet.items():
		print(k.title()+' : '+v)

#6-11 
cities = {'rome':	
				{'country':'Italy',
				'population':150250,
				'fact':'Tower of Pisa'
				},
		  'paris':
				{'country':'France',
				'population':75000,
				'fact':'Eiffel Tower'
				},
		   'karachi':
		   		{'country':'Pakistan',
		   		'population':200510,
		   		'fact':'Qaid e Azam'
		   		}
		   }
for city, info in cities.items():
	print(city.title())
	for k,v in info.items():
		print(k+' : '+str(v))









