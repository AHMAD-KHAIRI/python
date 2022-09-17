# 45. IndexErrors and working with nested lists
# Coded on 17.09.2022

# Recap on previous example
states_of_america = ["Delaware", "Pennsylvania"]
states_in_malaysia = ["Perlis", "Pulau Pinang", "Kedah", "Perak", "Selangor", "Kuala Lumpur","Pahang", "Terengganu", "Kelantan", "Negeri Sembilan", "Melaka", "Johor Bahru", "Sabah", "Sarawak"]

print(len(states_of_america))
print(len(states_in_malaysia))

# IndexError is when you go beyond the list size/ list index out of range
# print(len(states_in_malaysia[14]))

# Below example also outputs IndexError because the total length of the list is 14 but the index starts from 0 and ends at 13
# num_of_states = len(states_in_malaysia)
# print(states_in_malaysia[num_of_states])
# Solution to this:
num_of_states = len(states_in_malaysia)
print(states_in_malaysia[num_of_states - 1])


# https://www.ewg.org/foodnews/dirty-dozen.php
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Bell Peppers", "Cherries", "Peaches", "Pears", "Celery", "Tomatoes"]

# How to separate into fruits and vegetables
# How can we have a list within a list --> Nested list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Cherries", "Peaches", "Pears"]
vegetables = ["Spinach", "Kale", "Bell Peppers", "Celery", "Tomatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# output: [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Cherries', 'Peaches', 'Pears'], ['Spinach', 'Kale', 'Bell Peppers', 'Celery', 'Tomatoes']]

print(dirty_dozen[1][1])
# Above outputs "Kale" because [1][1] is referring to the vegetables list (index 1) and item with index no 1 in the list


# Exercise 3 - Treasure Map

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# input function will return a string, hence need to convert to int. Then need to deduct 1 because index no starts from 0 and ends at 2
row = int(position[0]) - 1
column = int(position[1]) - 1
map[column][row] = 'X'

# -------------------------------------------------------------------------------------
# Udemy trainer solution:
# horizontal = int(position[0])
# vertical = int(position[1])

# do like this:
# selected_row = map[vertical -1]
# selected_row[horizontal - 1] = 'X'
# or do like this:
# map[vertical -1][horizontal - 1] = 'X'
# -------------------------------------------------------------------------------------

# [0][1][2],[0][1][2],[0][1][2] --> actual list with index no. starting from 0
# [1][2][3],[1][2][3],[1][2][3] --> list for user with index no. starting from 1

# if user inputs the no. 23, then we place 'X' at:
# [0][1][2],[0][1][2],[0]['X'][2]
# [1][2][3],[1][2][3],[1]['X'][3]

# which becomes like this in a 3 x 3 matrix:
# [0] [1] [2],
# [0] [1] [2],
# [0] ['X'] [2]

# if user inputs 23 --> [row3][index no. 1] or map[2][1]
# [2][3] = column 2 aka row3, row 3 aka index no. 1
# column: 2 - 1 = 1
# row: 3 - 1 = 2
# output: [2][1]

# if user inputs 31 --> row1[index 2]
# 3 - 1 = 2
# 1 - 1 = 0
# output: [0][2]

# if user inputs 11 --> row1[index 0]
# 1 - 1 = 0
# 1 - 1 = 0
# output: [0][0]

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

