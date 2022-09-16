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



