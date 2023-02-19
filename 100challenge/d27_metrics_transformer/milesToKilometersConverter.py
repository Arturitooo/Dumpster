import tkinter

def calculate_miles_km():
    kilometers.config(text=float(input.get())*1.6)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height = 200)
window.config(padx=10, pady=10)


#Entry (input)

input = tkinter.Entry(width = 20)
#input.pack()
#input.place(x=100,y=200)
input.grid(column=1, row=0)
input.get()

#label
my_label = tkinter.Label(text="Miles", font=('Ariel', 16))
#my_label.pack() #it says to show the label in program
my_label.grid(column=2, row=0)

#label
is_equal = tkinter.Label(text="is equal to", font=('Ariel', 16))
#my_label.pack() #it says to show the label in program
is_equal.grid(column=0, row=1)

#label
kilometers = tkinter.Label(text="0", font=('Ariel', 16))
#my_label.pack() #it says to show the label in program
kilometers.grid(column=1, row=1)

#label
km = tkinter.Label(text="km", font=('Ariel', 16))
#my_label.pack() #it says to show the label in program
km.grid(column=2, row=1)

calculate = tkinter.Button(text="Click me", command=calculate_miles_km)
#button.pack()
calculate.grid(column=1, row= 2)
calculate.config(padx=10, pady=10)

window.mainloop()