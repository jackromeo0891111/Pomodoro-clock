from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer", font=("Times New Roman", 50), bg=YELLOW, fg=GREEN)
    label2.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_second = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_second)
        label1.config(text="long break", font=("Times New Roman", 50), bg=YELLOW, fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_second)
        label1.config(text="short break", font=("Times New Roman", 50), bg=YELLOW, fg=PINK)
    else:
        count_down(work_second)
        label1.config(text="working", font=("Times New Roman", 50), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if seconds == 0:
        seconds = "00"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
        label2.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Ariel", 35, "bold"))
canvas.grid(column=1, row=1)

label1 = Label(text="Timer", font=("Times New Roman", 50), bg=YELLOW, fg=GREEN)
label2 = Label(bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=0)
label2.grid(column=1, row=3)

button1 = Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
button2 = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
button1.grid(column=0, row=2)
button2.grid(column=2, row=2)

window.mainloop()
