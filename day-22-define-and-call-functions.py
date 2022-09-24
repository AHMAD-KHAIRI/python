# 59. Defining and calling Python functions
# Coded on 24.09.2022

# print() function
from cmd import PROMPT


print("Hello")

# len() function
num_char = len("Hello")
print(num_char)

# How to make our own funtion
# def name_of_function(input):
    # content of the function

def my_function():
    print("Hello AK!")

# Calling a function
# name_of_function()
my_function()

# Defining functions
# def my_function():
    # Do this
    # Then do this
    # Finally do this

# Calling functions
# my_function()

# 60. The hurdles loop challenge
# Source: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Solution:
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# for number in range (1, 7):
#     move()
#     jump()

# 61. Indentation in Python

# def my_function():
#     print("Hello")

def my_function1():
    sky = input("Is the sky clear or cloudy?")
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("Hello")

my_function1()

# In python, spaces are preferred than tabs

# The below example will give an indentation error
# def my_function2():
# print("Hello")

# my_function2()

# 62. While loops
# The loop that will continue going while in particular condition is true

# Comparison for loop vs while loop
# for item in list_of_items:         
    # Do something to each item

# for number in range(a, b):
    # print(number)

# while something_is_true:
    # Do something repeatedly

# while something_is_true:
    # Do this
    # Then do this
    # Then do this

# Reeborg's World Hurdle 1 while loop Exercise
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# Reeborg's World Hurdle 2 while loop Exercise 
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

#while at_goal() != True:
#    jump()

# Or we can do like this
# while not at_goal():
#     jump()


# for loop is used when there is a range to execute a condition
# use while loop when you don't care about number in the range and just want to execute a condition
# while loop is dangerous --> infinite loop

# 63. Hurdles challenge using while loops
# Reeborg's World Hurdle 3
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# # use front_is_clear() or wall_in_front(), at_goal() and their negation

# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()

# 64. Jumping over hurdles with variable heights
# Reeborg's world hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     elif front_is_clear():
#         move()


# 65. Final project: Escaping the Maze
# Revisit this challenge after completing intermediate Day 15
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
