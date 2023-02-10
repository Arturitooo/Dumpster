from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.5
STARTING_X_COORD = 300


class CarManager:
    def __init__(self):
        self.allcars = []
        self.move_speed = STARTING_MOVE_DISTANCE


    def generate_car(self):
        random_chance = random.randint(0,2)
        if random_chance == 1:
            newcar = Turtle("square")
            newcar.shapesize(stretch_len=2, stretch_wid=1)
            newcar.penup()
            newcar.goto(STARTING_X_COORD,random.randint(-290,290))
            newcar.color(random.choice(COLORS))
            self.allcars.append(newcar)


    def move_cars(self):
        for car in self.allcars:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.move_speed += MOVE_INCREMENT


"""

        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()

        self.y_move = -STARTING_MOVE_DISTANCE


    def generate_car(self):


        self.shape("circle")
        self.penup()
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
        self.pong()"""