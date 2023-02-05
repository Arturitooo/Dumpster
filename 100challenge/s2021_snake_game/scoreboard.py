from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align = "center", font=("Arial", 16, "normal"))
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align = "center", font=("Arial", 16, "normal"))
        self.hideturtle()
    
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"Game over!", align = "center", font=("Arial", 24, "bold"))
        self.hideturtle