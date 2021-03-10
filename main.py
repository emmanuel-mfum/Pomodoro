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
    start_button.config(state="normal")
    window.after_cancel(timer)  # cancel the after() method call in the timer variable
    canvas.itemconfig(timer_text, text="00:00")  # reset the time displayed
    title.config(text="Timer")  # reset the title displayed
    check_marks.config(text="")  # rest the checks marks
    reps = 0  # reset the number of reps
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():  # function be called upon start
    global reps
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Break", fg=RED)  # set the title to be displayed
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)  # set the title to be displayed
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)  # set the title to be displayed
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):  # we put the after method into a function in order to have a loop-like call to the function

    count_minutes = math.floor(count / 60)  # calculates the number of minutes
    count_seconds = count % 60  # calculated the number of seconds

    if count_seconds == 0:
        count_seconds = "00"  # thanks to Python dynamic typing
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"  # thanks to Python dynamic typing
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")  # change the text on the canvas

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # waits 1000 ms, then call the function and passes an arg
    else:
        window.attributes('-topmost', 1)  # brings the window at the top of the desktop
        window.attributes('-topmost', 0)  # brings the window at the top of the desktop
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)  # calculate the amount of work sessions (1 out of 2 reps)
        for _ in range(work_sessions):
            marks += "✔"  # add a check mark

        check_marks.config(text=marks)  # displays the check marks
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)  # adds padding to the window


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # width and height are in pixels
tomato_img = PhotoImage(file="tomato.png")  # reads the image and makes it a PhotoImage file
canvas.create_image(100, 112, image=tomato_img)  # the two first arguments are the x and y coordinate of image on canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)  # loads the canvas on the window


# Labels

title = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW)  # fg is used to color text and labels
title.grid(column=1, row=0)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


# Buttons

start_button = Button(text="Start", command=start_timer, state="normal")
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)


window.mainloop()
