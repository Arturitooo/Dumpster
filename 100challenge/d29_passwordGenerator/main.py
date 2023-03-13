from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_gen():
    pw.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    pw.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    wwebsite = website.get()
    eemail = email.get()
    ppw = pw.get()

    if len(wwebsite) == 0 or len(eemail) == 0 or len(ppw) == 0:
         messagebox.showinfo(title = "Oops", message = "You didn't provde all the necessary data. Please fulfill all of the fields")
    
    else:
        is_okay = messagebox.askokcancel(title=website, message = f"These are the details entered: \n Website: {wwebsite} \n Email: {eemail} \n Password: {ppw}")
        if is_okay:
                with open(r"C:\Users\Art\Documents\GitHub\learning\100challenge\d29_passwordGenerator\data.txt", "a") as data_file:
                    data_file.write(f"{wwebsite} | {eemail} | {ppw} \n")
                    website.delete(0,END)
                    email.delete(0,END)
                    pw.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=r"C:\Users\Art\Documents\GitHub\learning\100challenge\d29_passwordGenerator\logo.png")
canvas.create_image(100,100,image=logo_img)

canvas.grid(column = 1, row = 0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row= 1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row= 2)
pw_label = Label(text="Password:")
pw_label.grid(column=0, row= 3)


#entries
website = Entry(width = 35)
website.grid(column = 1, row = 1, columnspan = 2)
website.focus()
email = Entry(width = 35)
email.grid(column = 1, row = 2, columnspan = 2)
email.insert(0,"artur@mail.com")
pw = Entry(width = 21)
pw.grid(column = 1, row = 3)


#buttons
button_gp = Button(text="Generate Password", command = pw_gen) #/command=...
button_gp.grid(column=2, row= 3)

button_add = Button(text="Add", width=36, command = save) #/command=...
button_add.grid(column=1, columnspan=2 , row= 4)


window.mainloop()