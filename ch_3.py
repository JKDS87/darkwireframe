# 3.4 Guest List
print('Make a list of guests and invite them to dinner.')

dinner_guests = ['There are currently no guests.']
dinner_guests[0] = 'Bonnie'
dinner_guests.insert(0, 'Alice')
dinner_guests.append('Claire')
print(dinner_guests)

for name in dinner_guests:
	greeting = ('Hello, ' + name.title() + ', would you please attend ' + 
		'my dinner party?')
	print(greeting)

# 3.5 Changing Guest List
print('\nModify your list of guests, replacing a guest who cannot attend.')

print('Unfortunately, ' + dinner_guests[0].title() + ' is unable to attend.')
dinner_guests[0] = 'Ash'

for name in dinner_guests:
	greeting = ('Hello, ' + name.title() + ', would you please attend ' +
		'my dinner party?')
	print(greeting)

# 3.6 More Guests
print('\nPractice adding additional guests to the invitation list.')

print('\n"Additional seats have become available for the event."')
dinner_guests.insert(0, 'Andre')
dinner_guests.insert(2, 'Bailey')
dinner_guests.append('Caroline')

print("\nThe final guest list includes the following: ")
for name in sorted(dinner_guests):
	print("--" + name.title())

# 3.7 Shrinking Guest List
print('\nReduce the number of seats and reprint the guest list.')

print('Due to recent developments concerning a global pandemic, ' +
		'the dinner has been limited to two guests.\n')

to_remove = [0, 0, 1, -1]
for n in to_remove:
	removed_guest = dinner_guests.pop(n)
	print('Sorry, ' + removed_guest.title() +
		', but due to unexpected events we must cancel our invitation.')

print('\nRemaining guests:')
for guest in dinner_guests:
	print('Hello, ' + guest.title() + ' - despite limited availability, ' +
		'we would still like to extend an invitation for dinner.')

print('\nVerify list is empty:')
for name in range(0, len(dinner_guests)):
	del dinner_guests[0]
print(dinner_guests)
