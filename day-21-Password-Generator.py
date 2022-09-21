# 56. Day 5 Project: Create a Password Generator
# Coded on 21.09.2022

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# no_of_letters = len(letters)
# for letter in range(1, nr_letters + 1):
#     random_no_of_letters = random.randint(0, no_of_letters - 1)
#     random_letters = letters[random_no_of_letters]
#     print(random_letters, end="")

# no_of_symbols = len(symbols)
# for symbol in range(1, nr_symbols + 1):
#     random_no_of_symbols = random.randint(0, no_of_symbols - 1)
#     random_symbols = symbols[random_no_of_symbols]
#     print(random_symbols, end="")

# no_of_numbers = len(numbers)
# for number in range(1, nr_numbers + 1):
#     random_no_of_numbers = random.randint(0, no_of_numbers - 1)
#     random_numbers = numbers[random_no_of_numbers]
#     print(random_numbers, end="")

# Udemy trainer's solution:
# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for sym in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for sym in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

# password_to_list = list(password)
# random.shuffle(password_to_list)
# print("".join(password_to_list))


# Udemy trainer's solution:

password_list = []

for char in range(1, nr_letters + 1):
    # password_list += random.choice(letters)
    # or we can do like this
    password_list.append(random.choice(letters))

for sym in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)
    password_list.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
# print("".join(password_list))