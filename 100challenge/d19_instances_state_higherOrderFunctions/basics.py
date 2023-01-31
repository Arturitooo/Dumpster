from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_clockwise():
    tim.right(10)

def rotate_Cclockwise():
    tim.left(10)



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_Cclockwise)
screen.onkey(key="c", fun=tim.clear)
screen.onkey(key="h", fun=tim.home)
screen.exitonclick()


