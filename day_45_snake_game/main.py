# New program after Snake class is created and code is separated into main.py and snake.py:
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create a new snake object from the imported Snake Class
snake = Snake()
# Create a new food object from the imported (& inherited) Food class
food = Food()
# Create a new scoreboard object
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food using distance() and change food location randomly
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail (after slicing)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with tail (before slicing)
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

screen.exitonclick()

# Program below is before Snake class is created and code separated into main.py and snake.py:
'''
# Step 1: Create a snake body
# # Step 2: Move the snake
# # # Step 3: Control the snake
# # # # Step 4: Detect collision with food
# # # # # Step 5: Create a scoreboard
# # # # # # Step 6: Detect collision with wall
# # # # # # # Step 7: Detect collision with tail

# Step 0: import
# moved to snake.py
from turtle import Screen, Turtle
import time
# Step 0: setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# # Step 2:
screen.tracer(0)

# Step 1: Doing it the manual way:
# segment_1 = Turtle(shape="square")
# segment_1.color("white")
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(x=-20, y=0)
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(x=-40, y=0)

# Step 1: Alternately use a for loop:
# start by creating tuples of x and y coordinates
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# # Step 2:
segments = []

# then create a for loop
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
#     # # Step 2:
    segments.append(new_segment)



# # Step 2:
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
        # seg.forward(20)

    # # # Step 3:
    for seg_num in range(len(segments) - 1, 0, -1):
    # for seg_num in range(start=len(segments) - 1, stop=0, step=-1):
    # for seg_num in range(start=2, stop=0, step=-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

# Step 0:
screen.exitonclick()
'''