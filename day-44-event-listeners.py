# Methods of TurtleScreen/Screen: using screen events
# Examples: listen(), onkey() / onkeyrelease(), onkeypress(), onclick() / onscreenclick(), ontimer(), mainloop() / done()
 
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counterclockwise():
    tim.left(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

# Create an etch-a-sketch code
# Use W = Forwards, S = Backwards, A = Counter-clockwise, D = Clockwise, C = Clear drawing




"""
# recap from calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# below is known in python as higher order function
# fnction that can work with other function
def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(2, 3, add)
print(result)
"""