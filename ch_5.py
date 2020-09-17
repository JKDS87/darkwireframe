# Exercises from Chapter 5

# 5.1 Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 28
print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age >= 28? I predict True.")
print(age >= 28)

print("\nIs age <= 28? I predict True.")
print(age <= 28)

print("\nIs age < 28? I predicy False.")
print(age < 28)

print("\nIs age > 50? I predict False.")
print(age > 50)

# 5.2 More Conditional Tests
bike = 'suzuki'
print("\nDoes bike == 'suzuki'? I predict True.")
print(bike == 'suzuki')

bike = 'suZUkI'
print("\nDoes bike.lower() == 'suzuki'? I predict True.")
print(bike.lower() == 'suzuki')

age_f = 29
age_m = 31
print("\nIs age_f > age_m? I predict False.")
print(age_f > age_m)

print("\nIs age_f != age_m? I predict True.")
print(age_f != age_m)

print("\nIs age_f == age_m? I predict False.")
print(age_f == age_m)

print("\nIs age_f <= age_m? I predict True.")
print(age_f <= age_m)

print("\nIs age_f > 30 and age_m > 30? I predicy False.")
print(age_f > 30 and age_m > 30)

print("\nIs age_f > 30 or age_m > 30? I predict True.")
print(age_f > 30 or age_m > 30)

bikes = ['suzuki', 'yamaha', 'ducati']
print("\nIs Suzuki in the list? I predict True.")
print('suzuki'.lower() in bikes)

print("\nIs Harley-Davidson in the list? I predict False.")
print('harley-davidson'.lower() in bikes)

print("\nIs Indian NOT in the list? I predict True.")
print('indian'.lower() not in bikes)

# 5.3, 5.4 Alien Colors #1 & 2
alien_color = 'yellow'

if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
elif alien_color == 'red':
	points = 20

print("\nYou just earned " + str(points) + " points!")

# 5.5 Alien Colors #3
alien_color = 'green'
if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
elif alien_color == 'red':
	points = 20

print("\nYou just earned " + str(points) + " points!")


alien_color = 'red'
if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
elif alien_color == 'red':
	points = 20
print("\nYou just earned " + str(points) + " points!")

# 5.6 Stages of Life

if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'adolescent'
elif age < 20:
	stage = 'teenageer'
elif age < 65:
	stage = 'adult'
elif age >= 65:
	stage = 'elder'

age = 35
print("\nAt age " + str(age) + ", you would be classified as: " + stage + ".")

# 5.7 Favorit Fruit
favorite_fruits = ['mangoes', 'grapes', 'watermelon']

if 'mangoes' in favorite_fruits:
	print("\nYou really like mangoes!")
if 'apples' in favorite_fruits:
	print("\nApples? That's pretty boring for a favorite fruit.")
if 'watermelon' in favorite_fruits:
	print("\nWatermelon? You must live somewhere hot, huh?")
if 'bananas' in favorite_fruits:
	print("\nBananas? What are you, a monkey?")
if 'grapes' in favorite_fruits:
	print("\nA fruit of royalty and sign of impecable taste.")
