# ----- LIBRARIES -----
from tkinter import *
import math


# ----- CONSTANTS -----
PINK = "#e2979c"
RED = "e7305b"
GREEN = "#9bdeac"
# BLUE = "#7ec8e3"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ----- FUNCTIONS -----
# COUNTDOWN MECHANISM
def countdown(count):
    # to display the timer in minutes:seconds format e.g. 05:00
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # a way to display leading 0 is to use Python's dynamic typing by changing the data type from int to str
    # if count_min == 0:
    #     count_min = "00"
    # elif count_min < 10:
    #     count_min = f"0{count_min}"

    # if count_sec == 0:
    #     count_sec = "00"
    # elif count_sec < 10:
    #     count_sec = f"0{count_sec}"

    # canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # another way is to use format specifier e.g. ":02d"
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    # canvas.itemconfig(timer_text, text=count)
    if count > 0:
        global TIMER
        # in tkinter, there is an in-built method called after()
        # syntax: after(time_in_ms, calls_a_function, passes_an_input_to_the_function)
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        # add the check mark sign every work reps completed
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✓"
            checkmark_label.config(text=marks)
    # print(count)

# TIMER MECHANISM
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif REPS % 2 == 0:
        # If it's the 2nd/4th/6th rep:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        # If it's the 1st/3rd/5th/7th rep:
        timer_label.config(text="Work")
        countdown(work_sec)
    
    print(f"reps:{REPS}")
    # Call the timer countdown function
    # countdown(1 * 60)

# TIMER RESET MECHANISM
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config("")
    global REPS
    REPS = 0


# ----- UI SETUP -----
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Create canvas widget:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# highlighthickness = 0 removes the default white outline
# Add an image to the canvas
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
# Add a text to the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Add the Timer label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
# fg: foreground changes the color of the label
timer_label.grid(column=1, row=0)

# Add the Start Timer button
start_button = Button(text="Start", width=10, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Add the Reset Timer button
reset_button = Button(text="Reset", width=10, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Add the ✓ / ✅ label
checkmark_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()
