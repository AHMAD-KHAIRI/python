import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # Create a tuple:
    color = (r, g, b)
    return color

tim.speed("fastest")

# create a function 
def draw_spirograph(size_of_gap):
    # create a loop
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(int(input("Enter size: ")))

screen = t.Screen()
screen.exitonclick()