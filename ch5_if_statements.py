cars = ['bmw','audi','merc','lexus']
if 'bmw' in cars:
    print('BMW is in the list')
if 'ferarri' not in cars:
    print('Youre too poor')
if 'bmw' in cars and 'lexus' in cars:
    print('this works too')

#Alien_Colour
alien_colour = 'green'
if alien_colour == 'green':
    print('5 points!')
alien_colour = 'yellow'
if alien_colour == 'green':
    print('5 points!')

alien_colour = 'green'
if alien_colour == 'green':
    print('5 points!')
else:
    print('10 points!')

alien_colour = 'yellow'
if alien_colour == 'green':
    print('5 points!')
else:
    print('10 points!')

#Stages of life
age = 12
if age < 2:
    print('Baby')
elif age >= 2 and age < 4:
    print('Toddler')
elif age >= 4 and age < 13:
    print('Kid')
elif age >= 13 and age < 20:
    print('Teen')
elif age >= 20 and age <65:
    print('Adult')
else:
    print('Elder')

#Usernames
usernames = ['Eric','Matt','Admin','Stacey','Leia']
if usernames:   #Check that usernames is not empty
    for username in usernames:
        if username.lower() == 'admin':
            print('Hello '+username+', status report?')
        else:
            print('Hello '+username)
else:
    print('Empty users') 

#Website
current_users = ['Dameon','Percy','Dan','Elena','Bart']
new_users = ['Elena','Matt','Susan','Dan','Christine']
if current_users and new_users:
    current_users_lower = [user.lower() for user in current_users]  #create case insensitive lists
    new_users_lower = [user.lower() for user in new_users]
    for username in new_users_lower:
        if username in current_users_lower:
            print('Already exists')
        else:
            print('Available')


#