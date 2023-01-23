from turtle import *
import random

"""timmy = Turtle()
colors = ['red', 'black', 'yellow', 'pink', 'brown', 'purple', 'blue', 'cyan', 'blue','orange','grey']
timmy.shape("turtle")"""

#task1
"""timmy.forward(125)
timmy.left(90)
timmy.forward(125)
timmy.left(90)
timmy.forward(250)
timmy.left(90)
timmy.forward(250)
timmy.left(90)
timmy.forward(250)
timmy.left(90)
timmy.forward(125)"""

#task2
"""for i in range(25):
    timmy.forward(6)
    timmy.penup()
    timmy.forward(6)
    timmy.pendown()"""

#task3
"""for i in range(3,11):
    timmy.color(random.choice(colors))
    for x in range(0,i):
        uncle = (360/i)
        timmy.forward(75)
        timmy.right(uncle)"""


#task4
#random walk, random colors, thickness, speedup turtle

"""dist = 25
angle = [0, 90, 180, 270]
timmy.speed('fastest')

for i in range(250):
    chosen_angle = random.choice(angle)
    timmy.right(chosen_angle)
    timmy.color(random.choice(colors))
    timmy.pensize(2+i/100)
    timmy.forward(dist)"""

#task5
#draw spirograph

"""timmy.speed('fastest')
timmy.circle(80)
for i in range(0,120,2):
    timmy.color(random.choice(colors))
    timmy.setheading(i*3)
    timmy.circle(120)

screen = Screen()
screen.exitonclick()"""

# Extract 6 colors from an image.
#how to get RGB colors with loop
#import colorgram

#colors = colorgram.extract(r'C:\Users\Art\Documents\GitHub\learning\100challenge\d18_turtle_GUI\image.jpg', 10)

#rgb_colors = []
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

#print(rgb_colors)


color_list = [(198, 12, 32), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]

#10 x 10 dots
#size dots 20
#distance 50

tim = Turtle()
colormode(255)
tim.speed('fastest')
tim.hideturtle()
for x in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)
    tim.pendown()

screen = Screen()
screen.exitonclick()
