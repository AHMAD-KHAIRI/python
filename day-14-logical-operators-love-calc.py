# 36. Logical Opertors
# Coded on 08.09.2022

# Recap if else statement
# if condition:
#   do this
# else condition:
#   do this

# to check multiple conditions in the same line of code
# if condition1 & condition2 & condition3:
#   do this
# else:
#   do this

# Logical operators:
# and operator : A and B --> A & B
# or operator : C or D  --> C | D
# not operator : not E   --> !E

# Exercise 5 - Love Calculator

# 🚨 Don't change the code below 👇
from re import T


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Hint: 
# 1. Use lower() function to change all letters in a string to lowercase e.g. "Khairi".lower() outputs "khairi"
# 2. Use count() function (beware case sensitive) to give the number of times a letter occurs in a string e.g. "Khairi".count("a") outputs 1

names = name1.lower() + name2.lower()
# print(names)

# test names: Ahmad Khairi Bin Hamzah and Sumaiyyah Binti Omar
# T 1
# R 2
# U 1
# E 0
# Sum: 4 

# L 0
# O 1
# V 0
# E 0
# Sum: 1
# Total: 41 

sum_t = names.count('t') 
sum_r = names.count('r')
sum_u = names.count('u')
sum_e = names.count('e')
sum_true = sum_t + sum_r + sum_u + sum_e

sum_l = names.count('l')
sum_o = names.count('o')
sum_v = names.count('v')
sum_e1 = names.count('e')
sum_love = sum_l + sum_o + sum_v + sum_e1

sum_true_love_str = str(sum_true) + str(sum_love)
sum_true_love_int = int(sum_true_love_str)

# print(sum_true_love_int)

if sum_true_love_int < 10 or sum_true_love_int > 90:
    print(f"Your score is {sum_true_love_int}, you go together like coke and mentos.")
elif sum_true_love_int >= 40 and sum_true_love_int <= 50:
    print(f"Your score is {sum_true_love_int}, you are alright together.")
else:
    print(f"Your score is {sum_true_love_int}.")

