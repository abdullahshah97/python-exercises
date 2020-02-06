#Operating on lists, del insert pop and remove
guest_list = ['Muhammad Ali', 'Emma Stone', 'Stan Lee']
message = 'Dear '+guest_list[0]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[1]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[2]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
#Returns removed element
cant_come = guest_list.pop(2)
#Inserting, into erd element
guest_list.insert(2,'Christoper Nolan')
message = 'Dear '+guest_list[0]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[1]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[2]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
print(cant_come+' cannot make it.')
#Inserting more guests, kate beckinsale at the end
guest_list.insert(1,'Edgar Wright')
guest_list.insert(2,'Simon Pegg')
guest_list.append('Kate Beckinsale')
message = 'Dear '+guest_list[0]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[1]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[2]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[3]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[4]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)
message = 'Dear '+guest_list[5]+'\nYou have been formally invited to attend my dinner party.\nWarmest regards,\n\tAbdullah Shah'
print(message)

print('Unfortunatley I can only invite 2 people now')
edgar = guest_list.pop(1)
simon = guest_list.pop(1)
chris = guest_list.pop(2)
print('Sorry '+edgar+". We're booked up, on your bike mate.")
print('Sorry '+simon+". We're booked up, on your bike mate.")
print('Sorry '+chris+". We're booked up, on your bike mate.")
print('Hi '+guest_list[0]+". You're still invited")
del guest_list[0]
print('Hi '+guest_list[0]+". You're still invited")
del guest_list[0]
print('Hi '+guest_list[0]+". You're still invited")
del guest_list[0]

#Seeing the world, sorting and other operations
places = ['Stars','Mountains','Beaches','Babylon','Giza']
print(places)
#Doesnt change actual order
print(sorted(places))
print(sorted(places, reverse= True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print (places)
print(len(places))








