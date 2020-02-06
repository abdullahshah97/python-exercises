import json

numbers = [2, 5, 6, 9, 11, 42]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

with open(filename) as f_obj:
	number = json.load(f_obj)

print(number)