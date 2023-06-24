from turtle import Turtle
import random

# steps to do class inheritance
# Step 1: Create the new class --> class Food:
# Step 2: Add a () after the class name --> class Food():
# Step 3: Add the superclass name / Put in the name of the class that we want to inherit from --> class Food(Turtle):
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # 0.5 will give the circle a size of 10 x 10 --> 20 * 0.5 = 10
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
