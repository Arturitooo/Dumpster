from turtle import Turtle
import random


class paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
        random_X = 350
        random_Y = random.randint(-250,250)
        self.goto(random_X, random_Y)
    
class paddle2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
        random_X = -350
        random_Y = random.randint(-250,250)
        self.goto(random_X, random_Y)

    def refresh(self):
        random_X = random.randint(-280,280)
        random_Y = random.randint(-280,280)
        self.goto(random_X, random_Y)