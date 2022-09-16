# 43. Understanding the Offset and Appending Items to Lists
# Coded on 16.09.2022

# Lists = Data structure
# A way of organizing and storing data

# a = 3
# b = "Hello"

# Order in data structure

# List:
# Always starts with [ and ends with ]
# fruits = [item1, item2]
# fruits = ["Cherry", "Apple", "Pear"]

# Store all of the names of the states in the US

# How we do it before, storing 1 data in 1 variable
state1 = "Delaware"
state2 = "Pennsylvania"

# With List we can do like this:
# states_of_america = [state1, state2]
states_of_america = ["Delaware", "Pennsylvania"]

# Order is determined in the order in the list aka Delaware first then Pennsylvania second

# How to retrieve data from list: use [n] where n = 0,1,2,...
print(states_of_america[0])

# using minus index where -1 starts from the last item in the list
print(states_of_america[-1])

# Alter data in the list:
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# Add an item at the end of the list --> Use .append function (adds single item at the end of the list)
states_of_america.append("AKland")
print(states_of_america)

# .extend function extend the list by appending more than 1 item
states_of_america.extend(["Imanland", "Hypersonic"])
print(states_of_america)


# Exercise 2 - Banker Roulette

# Important: You are not allowed to use the choice() function.

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# num_of_items = len(names)
# random_choice = random.randint(0, num_of_items - 1)
# person_to_pay = names[random_choice]
# print(f"{person_to_pay} is going to buy the meal today!")

# Udemy trainer solution:
# Get the total number in the list using len()
num_items = len(names)

# Get the random number from the list using random.randint
random_choice = random.randint(0, num_items - 1)
# print(random_choice)

# Use the random number to generate the random index number
person_who_will_pay = names[random_choice]

# Print the output to console
print(person_who_will_pay + " is going to buy the meal today!")

# Alternatively, we can use the function choice()
# random_names = random.choice(names)
# print(names, random_names)
# print(f"{random_names} is going to buy the meal today!")

