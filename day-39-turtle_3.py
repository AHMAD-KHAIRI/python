# 169. Turtle challenge 3 - drawing different shapes

import turtle as t
import random

tim = t.Turtle()

# First learn how to draw a shape:

# Example: Draw an Octagon
# num_sides = 5
# Example: Dekagon
# num_sides = 10

# for _ in range(num_sides):
#     angle = 360 / num_sides
#     tim.forward(100)
#     tim.right(angle)

# ---------------------------------------------------------------------------

# Second: Define a function to draw a shape

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)

# ---------------------------------------------------------------------------

# Third: Draw a shape but with different line colors

colors = ["cyan", "medium aquamarine", "forest green", "dark orange", "magenta", "medium purple", "gold"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


# ---------------------------------------------------------------------------

# Next idea: Prompt user to input a shape e.g. square, triangle, rectangle, etc