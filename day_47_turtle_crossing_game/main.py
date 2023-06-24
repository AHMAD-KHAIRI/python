from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width= 600, height= 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.move_cars()

    # Detect collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_back_to_start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()