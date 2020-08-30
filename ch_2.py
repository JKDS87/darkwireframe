# 2.4 Name Cases
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# 2.5 Famous Quote
name = "katagiri roshi"
quote = "Whatever you think is delusion."
message = "As " + name.title() + " once said, \"" + quote + "\""

print(message)

# 2.6 Famous Quote 2
name = "Hannibal lecter"
quote = "You would take away my life?"
message = "In the words of " + name.title() + ', "' + quote + '"'
print(message)

# 2.7 Stripping Names
name_1 = "  Matthew  "
name_2 = " \tMegan "
name_3 = "  \nElla\t "

print(name_1, name_2, name_3)
print(name_1.strip())
print(name_2.strip())
print(name_3.strip())

# 2.8 Number Eight
a = 4 + 4
b = 9 - 1
c = 16 / 2
d = 4 * 2
print(a, b, c, d)

# 2.9 Favorite Number
favorite_number = 13
message = "My favorite number is " + str(favorite_number) + "."
print(message)
