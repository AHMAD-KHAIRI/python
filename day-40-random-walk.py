import turtle as t
import random

tim = t.Turtle()

colors = ["cyan", "medium aquamarine", "forest green", "dark orange", "magenta", "medium purple", "gold"]
directions = [0, 90, 180, 270]
# where 0 = East, 90 = North, 180 = West, 270 = South

# # first part: generate random walk
# for _ in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# # second part: generate random colors
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# third part: increase the line thickness
tim.pensize(15)

# random number generator
# random_integer = random.randint(1, 100)

for _ in range(200):
    # tim.pensize(random_integer)
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

# fourth part: increase the speed
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))