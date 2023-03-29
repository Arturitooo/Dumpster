from tkinter import *
import requests

def get_quote():
    #this functions is hitting api to get Kanye West famous quote
    response = requests.get('https://api.kanye.rest/')
    #response handling thing
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text = quote)



window = Tk()
window.title('Kanye says...')
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"C:\Users\Art\Documents\GitHub\learning\100challenge\d33_playingWithAPIandJSON\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 190, text='Kanye quote goes here', width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"C:\Users\Art\Documents\GitHub\learning\100challenge\d33_playingWithAPIandJSON\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
