BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
import json

# ---------------------------- Reading from CSV with Pandas ------------------------------- #

try:
    data = pandas.read_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d31_flashCardProgram\data\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d31_flashCardProgram\data\french_words.csv")
finally:
    database = data.to_dict(orient='records')
current_card = {}

def next_card():
    canvas.itemconfig(card_front, image = card_front_img)
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(database)
    canvas.itemconfig(card_title, text = "French", fill = 'black')
    canvas.itemconfig(card_word, text = current_card['French'], fill = 'black')
    flip_timer = window.after(2000, func = card_flip)

def card_flip():
    canvas.itemconfig(card_front, image = card_back_img)
    canvas.itemconfig(card_title, text = "English", fill = 'white')
    canvas.itemconfig(card_word, text = current_card['English'], fill = 'white')

def is_known():
    database.remove(current_card)

    words_to_learn = pandas.DataFrame(database)
    words_to_learn.to_csv(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d31_flashCardProgram\data\words_to_learn.csv")

    next_card()

def answer_unknown():
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(width = 800, height= 526, padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(2000, func = card_flip)

#canvas
canvas = Canvas(width = 800, height=526)
card_back_img = PhotoImage(file=r"C:\Users\Art\Documents\GitHub\learning\100challenge\d31_flashCardProgram\images\card_back.png")
card_front_img = PhotoImage(file=r"C:\Users\Art\Documents\GitHub\learning\100challenge\d31_flashCardProgram\images\card_front.png")
card_front = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400, 150, text = "Title", font = ('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text = "word", font = ('Ariel', 60, 'bold'))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#images
photo_correct_img = PhotoImage(file = r"C:\Users\Art\Documents\GitHub\learning\100challenge\d31_flashCardProgram\images\right.png")
correct_button = Button(text="Right", image = photo_correct_img, highlightthickness=0, command= is_known)
correct_button.grid(row=1, column=1)

photo_wrong_img = PhotoImage(file = r"C:\Users\Art\Documents\GitHub\learning\100challenge\d31_flashCardProgram\images\wrong.png")
wrong_button = Button(text="Wrong", image = photo_wrong_img, highlightthickness=0, command= next_card)
wrong_button.grid(row=1, column=0)


next_card()


window.mainloop()