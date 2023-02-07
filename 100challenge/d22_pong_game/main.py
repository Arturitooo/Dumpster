#create the screen
#wall nr1 / paddle
#wall nr2 / paddle
#moving walls
#ball_moving 
#ball bouncing walls
#ball bouncing paddle
#score

from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((375,0))
l_paddle = Paddle((-375,0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
