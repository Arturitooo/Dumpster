import tkinter

def button_clicked():
    my_label.config(text=input.get()) #another one way to change something in label


window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width = 500, height = 300)
window.config(padx=10, pady=10)

#label
my_label = tkinter.Label(text="I am a label", font=('Ariel', 24, "bold"))
#my_label.pack() #it says to show the label in program
my_label.grid(column=0, row=0)

my_label["text"]="new text" #one way to change something in label
my_label.config(text="super new text") #another one way to change something in label

#Button

button = tkinter.Button(text="Click me", command=button_clicked)
#button.pack()
button.grid(column=1, row= 1)
button.config(padx=10, pady=10)

button2 = tkinter.Button(text="Click me", command=button_clicked)
#button.pack()
button2.grid(column=2, row= 0)

#Entry (input)

input = tkinter.Entry(width = 25)
#input.pack()
#input.place(x=100,y=200)
input.grid(column=3, row=2)
input.get()

#this one keeps program running :) 
window.mainloop()

#there are 3 layout managers
#pack - basically packs everything one under another
#place - you provide specific X, y coord
#grid - you have columns and rows - table shape - you cannot mix grid and pack!!