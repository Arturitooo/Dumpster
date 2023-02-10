import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
level = 1

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.generate_car()
    carmanager.move_cars()

    for car in carmanager.allcars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor()>= 285:
        scoreboard.level_up()
        carmanager.level_up()
        time.sleep(0.5)
        player.next_level()

screen.exitonclick()