from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
    
    def pong(self):
        self.x_move *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.pong()

