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


def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark["text"] = ""
    timer_label["text"] = "TIMER"
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(long_break)
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=RED)
        count_down(short_break)
    else:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)


def count_down(count):
    seconds = count % 60
    minutes = int(math.floor(count / 60))
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        tick = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            tick += "✔"
        check_mark.config(text=tick)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="TIMER", font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", fg="white", bg=PINK, font=(FONT_NAME, 10, "bold"), command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", fg="white", bg=PINK, font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset.grid(column=2, row=2)


check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "normal"))
check_mark.grid(column=1, row=3)

window.mainloop()
