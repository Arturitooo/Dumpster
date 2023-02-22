from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0 
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text = f"00:00")
    checkmarks.config(text = "")
    reps = 0

     
 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg = RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += checkmark 
            checkmarks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg = GREEN, font=('Ariel', 40, "bold"), bg=YELLOW)
timer_label.grid(column=1, row= 0)

canvas = Canvas(width = 200, height=224, bg=YELLOW, highlightthickness =0)
tomato_image = PhotoImage(file=r"C:\Users\Art\Documents\GitHub\learning\100challenge\d28_pomodoro\tomato.png")
canvas.create_image(101,112, image = tomato_image)
timer_text = canvas.create_text(101,132,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row= 1)

button_start = Button(text="Start", bg = "white", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row= 2)

button_stop = Button(text="Reset", bg = "white", highlightthickness=0, command = reset_timer)
button_stop.grid(column=2, row= 2)

checkmark = "✔"
checkmarks = Label(fg = GREEN, font=('Ariel', 15, "bold"), bg=YELLOW)
#my_label.pack() #it says to show the label in program
checkmarks.grid(column=1, row= 3)

window.mainloop()