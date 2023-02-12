import turtle
import pandas

states = pandas.read_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d25_pandas_basics\us_states_game\50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
t = turtle.Turtle()
image = r"C:\Users\Art\Documents\GitHub\learning\100challenge\d25_pandas_basics\us_states_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t.penup()
t.hideturtle()
score = 49
game_is_on = True

all_states = states.state.to_list()

while game_is_on:
    answer_state = (screen.textinput(title=f"{score}/50 States guessed", prompt = "Try to guess another state")).capitalize()
    if answer_state in all_states:
        state_data = states[states.state == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state_data["state"].item())
        all_states.remove(answer_state)
        score += 1
    else:
        pass

    if score == 50:
        t.goto(0,0)
        t.write("Congratulations, you know all the states!", True, align="center", font=("Arial", 18, "bold"))
        game_is_on = False
