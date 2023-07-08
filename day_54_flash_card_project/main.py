# ------------------------------ LIBRARIES ------------------------------
from tkinter import *
import pandas, random


# ------------------------------ CONSTANTS ------------------------------
BACKGROUND_COLOR = "#B1DDC6"
TIMER = None
current_word = {}
to_learn = {}


# ------------------------------ FUNCTIONS ------------------
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    # put the word into the text
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"],fill="black")
    canvas.itemconfig(card_background, image=flash_card_front_image)
    flip_timer = window.after(3000, func=flip_card)
    

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")
    canvas.itemconfig(card_background, image=flash_card_back_image)

def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------ UI SETUP ------------------------------
# Setup the window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady= 50, background=BACKGROUND_COLOR)

# setup the function to flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Create the canvas widget
canvas = Canvas(width=800, height=526)
flash_card_front_image = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=flash_card_front_image)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
flash_card_back_image = PhotoImage(file="./images/card_back.png")

# Create the text widgets
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Create the button widgets
right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)

# Position the widgets
canvas.grid(row= 0, column=0, columnspan=2)
wrong_button.grid(row= 1, column=0)
right_button.grid(row= 1, column=1)

# include exception handling
try:
    # read csv file using pandas
    data = pandas.read_csv("./data/words_to_learn.csv")
    # data = pandas.read_csv("./data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # convert the df to a dictionary and use the parameter orient=‘records’ --> list like [{column -> value}, … , {column -> value}]
    to_learn = data.to_dict(orient="records")


# call the function
next_card()

# keep the window opened
window.mainloop()