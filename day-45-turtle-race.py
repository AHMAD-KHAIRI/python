from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["black", "red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [180, 120, 60, 0, -60, -120, -180]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        # check if turtle have reached the finish line
        if turtle.xcor() > 230:
        # Why 230? 250 - (40 / 2 ) where 250 is max. x position and 40 is turtle width divide 2 to get centre point
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")

        # randomly move the turtle forward
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()