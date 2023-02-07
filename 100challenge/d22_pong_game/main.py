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
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((375,0))
l_paddle = Paddle((-375,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    
    scoreboard
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        #needs to bounce
        ball.bounce()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -350 or ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.pong()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
