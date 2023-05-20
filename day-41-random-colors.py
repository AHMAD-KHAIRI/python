import turtle as t
import random

# Python tuple is a data type in python and it looks like this: (1, 3, 8) 
# where each of the items inside the bracket is separated by a comma.
# A Python list looks like this: [1, 3, 8]
# What is the difference? You can't change the values in a tuple like you can in a list
# If you try to change it, you will get the TypeError: 'tuple' object does not support item assignment
# Hence, a tuple is immutable
# Example:
# my_tuple = (1, 3, 8)

# print(my_tuple[0])
# output: 1
# print(my_tuple[1])
# output: 3
# print(my_tuple[2])
# output: 8

# my_tuple[0] = 2
# print(my_tuple[0])
# output: TypeError

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Create a tuple:
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))