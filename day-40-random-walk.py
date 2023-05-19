import turtle as t
import random

tim = t.Turtle()

colors = ["cyan", "medium aquamarine", "forest green", "dark orange", "magenta", "medium purple", "gold"]
directions = [0, 90, 180, 270]
# where 0 = East, 90 = North, 180 = West, 270 = South

for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))