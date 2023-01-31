from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height=400)

colors = ['red','orange','yellow','green','purple','blue']
all_turtles = []

for turtle_index in range(0,6):
    #loop creates 6 turtles with different color and home position
    new_turtle = Turtle(shape="turtle")
    color = random.choice(colors)
    color_index = colors.index(color)
    colors.pop(color_index)
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-240,y=((125-50*turtle_index)))
    new_turtle.pendown()
    all_turtles.append(new_turtle)

bet = screen.textinput(title="The Winner", prompt = "What color turtle will win the game?")

if bet:
    is_race_on = True

while is_race_on == True:
    #this is were the competition begins ^^
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if bet == turtle.pencolor():
                print("Congratulations, you guessed the winner!")
            else:
                print(f"You were wrong!, the {turtle.pencolor()} turtle won the race!")
        rand_distance = random.randint(0,10)
        turtle.penup()
        turtle.forward(rand_distance)
        turtle.pendown()
    
    


screen.exitonclick()