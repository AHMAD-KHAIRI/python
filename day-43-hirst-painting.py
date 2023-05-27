# Part 1 - Extracting the RGB values
''' 
import colorgram

# create an empty list
rgb_colors = []

# Extract 6 colors from an image.
colors = colorgram.extract('hirst_spot.jpg', 30)
# print(colors)

for color in colors:
    # rgb_colors.append(color.rgb)
    
    # separate the color
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    # create a tuple
    new_color =(r, g, b)

    # add to rgb_colors
    rgb_colors.append(new_color)


print(rgb_colors)
'''

# Part 2 - Drawing the Dots

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

# extracted rgb values from part 1 and saved in a list
color_list = [(230, 233, 239), (239, 231, 235), (227, 236, 230), (198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39), (131, 37, 27)]

# hide the turtle aka arrow
tim.hideturtle()

# adjust speed
tim.speed("fastest")
# hide the pen lines
tim.penup()
# set heading direction
tim.setheading(225)
# move 300 steps
tim.forward(300)
# set heading back to normal
tim.setheading(0)
# print out 100 dots
number_of_dots = 100


# create a loop
for dot_count in range(1, number_of_dots + 1):
    # use the turtle dot() function to draw a circular dot with the given size
    # randomly choose from the color_list
    tim.dot(20, random.choice(color_list))
    # then move forward
    tim.forward(50)

    # create condition where after printing 10 dots, move to a new line
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# use the turtle screen and exitonclick() function to exit from the screen if and only if the mouse is clicked.
screen = turtle_module.Screen()
screen.exitonclick()