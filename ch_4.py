# Practice exercises from chapter 4

# 4.1 Pizzas 
pizzas = ['sausage mushroom', 'meat lovers', 'barbeque chicken']
for pizza in pizzas:
	print("I enjoy " + pizza + " pizza.")
print("I really enjoy different types of pizza!")

# 4.2 Animals
animals = ['walrus', 'tiger', 'wolly mammoth']

print("\n" + animals[0].title() + "es like to live in cooler climates.")
print(animals[1].title() + "s are very majestic.")
print(animals[2].title() + "s are no longer found living anywhere on Earth.") 
print("Each of these animals features large tusks.")

# 4.3 Counting to Twenty
numbers = [n for n in range(1, 21)]
print(numbers)

# 4.4 One Million
million = [n for n in range(1, 1000001)]
#for number in million:
	# print(number)

# 4.5 Summing a Million
million = [n for n in range(1, 10000001)]
print("\nFirst number: " + str(min(million)))
print("Last number: " + str(max(million)))
print("Sum of numbers 1 - 1,000,000: " + str(sum(million)))

# 4.6 Odd Numbers
odd_numbers = [n for n in range(1, 21, 2)]
print("\nOdd numbers 1-20: ")
for number in odd_numbers:
	print(number)
	
# 4.7 Threes
by_threes = [n for n in range(3, 31, 3)]
print("\nCounting by threes, 3 - 30: ")
for number in by_threes:
	print(number)

# 4.8 (and 4.9) Cube Comprehension
cubes = [value**3 for value in range(1, 11)]
print("\nCubes of numbers 1 - 10:")
for n in cubes:
	print(n)

# 4.10 Slices
odd_numbers = [n for n in range(1, 21, 2)]
print("\nThe first three items in the list of odd numbers are:")
print(odd_numbers[:3])
print("Three items from the middle of the list are:")
print(odd_numbers[2:5])
print("The last three items in the list are:")
print(odd_numbers[-3:])

# 4.11 My Pizzas, Your Pizzas
pizzas = ['sausage mushroom', 'meat lovers', 'barbeque chicken']
friend_pizzas = pizzas[:]

friend_pizzas.append('hawaiian')
pizzas.append('bacon and mushroom')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)

# 4.12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('canoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are: ")
for food in my_foods:
	print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)

# 4.13 Buffet
buffet = ('fried rice', 'sweet and sour pork', 'crab rangoons',
	'orange chicken', 'dumplings')
print("\nOriginal buffet lineup:")
for food in buffet:
	print(food)

buffet = ('fried rice', 'lo mein', 'crab rangoons', 'dumplings', 'chow mein')
print("\nUpdated buffet lineup:")
for food in buffet:
	print(food)
