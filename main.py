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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)
REPS = 0
TICKING = None


def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="BREAK")
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="BREAK")
    elif REPS % 2 != 0:
        count_down(WORK_MIN * 60)
        title_label.config(text="WORK")


def count_down(count):
    global TICKING
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"{0:}{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:  # window.after method calls count_down method after every 1000 ms, count-1 is argument of count_down
        TICKING = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        text = ""
        no_reps = math.floor(REPS / 2)
        for _ in range(no_reps):
            text += "✔\n "
        check_mark.config(text=text)


def restart_time():
    global TICKING
    global REPS
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(TICKING)
    REPS = 0
    start_timer()


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))  # fg is for colour of the text
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # to get hold of tomato.png
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=restart_time)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, background=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()  # to keep window on screen otherwise it will close immediately
