# importing modules
# Method #1: import the complete module
# import turtle
# Method #2: 
from turtle import Turtle, Screen
# Method #3: using *
# from turtle import *
# Note: using * will import everything in the module but avoid to use it
# Method #4: using alias name
# import turtle as t

# Installing packages
# import heroes


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

# # Exercise: Draw a square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# # simplify using for loop
# for move in range (4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Exercise: Draw a dashed line
for _ in range (15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

# Move this code to the end
screen = Screen()
screen.exitonclick()