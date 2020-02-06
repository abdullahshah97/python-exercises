# Deli sandwiches
sandwiches = ['meatball sub', 'pastrami', 'burgers', 'blt', 'veggie','pastrami', 'pastrami']
finished_sandwiches = []
while sandwiches:
	finished_sandwiches.append(sandwiches.pop())
	print('finished making your '+finished_sandwiches[-1])
#You can also use a variable for .pop() probably better to, I just wanted to practice
print('all sandwiches made')

sandwiches = finished_sandwiches[:]
finished_sandwiches=[]
print("we've run out of pastrami, run the orders by me again")
while 'pastrami' in sandwiches:
	sandwiches.remove('pastrami')

while sandwiches:
	current = sandwiches.pop()
	finished_sandwiches.append(current)
	print('finished making your '+finished_sandwiches[-1])
print('all sandwiches made')
print 

# creating a dictionary for persons details
repeat = ''
people_dream={}
while repeat!= 'no':
	entry = input('what is your name? \n')
	people_dream[entry] = input('where would you like to go for your dream vacation?' )
	repeat = input('are there more people?\n')

for person, dream in people_dream.items():
	print(person+' would like to go to '+dream)

