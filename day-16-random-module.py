# 41. Random Module
# Coded on 11.09.2022

# Python random module based on Mersenne Twister

# First need to import the random module
from cmath import pi
import random
# import day-16-my_module

random_integer = random.randint(1, 10)
print(random_integer)

# What is a module?
# Each module is responsible for a specific functionality of your program

# print(day-16-my_module.pi) --> doesn't work
print(pi)

# random floating number
random_float = random.random()
print(random_float)

# random decimal number between 0 and 5?
random_decimal = random.randint(0, 5)
print(random_decimal)

# generate random float number between 0.0000000 - 4.9999999...
randomFloat = random.random() * 5
print(randomFloat)

# what can we do with random nummbers?
# roll a dice, flip a coin

# Exercise 1 - Heads or Tails
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
dice = random.randint(0, 1)
print(dice)

if dice == 1:
    print("Heads")
else:
    print("Tails")
