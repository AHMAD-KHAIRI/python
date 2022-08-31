# Coded on 31.08.2022
# 29. Control flow with if / else and Conditional Operators
# if condition:
#   do this
# else:
#   do this

# for example water that is filling in a bath tub: 
# water_level = 50
# if water_level > 80:
#   print("Drain water")
# else:
#   print("Continue")

# Exercise #1: Rollercoaster ride height
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Check if the height is greater than 120cm to play the rollercoaster
if height >= 120:
    print("You can ride the rollercoaster!")
# make sure that else is not indented over but must be placed the same indent as the if statement
else:
    print("Sorry, you have to be taller than 120cm to ride the rollercoaster! ")

# Comparison operators
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# == : Equal to
# != : Not equal to

# Day 3 Exercise 1 - Odd or Even
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")