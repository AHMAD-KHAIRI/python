# ----- IMPORT LIBRARIES -----
from tkinter import *
import random


# ----- CONSTANTS -----


# ----- FUNCTIONS -----
def add_data():
    website = website_input.get()
    email = email_or_username_input.get()
    password = password_input.get()
    print(website, email, password)
    
    # for entry in data:
        # everytime the add button is pressed, append/insert new data into file
    # creates new letter for every name and write the content of the letter
    # with open(f"data.txt", mode="w") as inserted_data:
        # inserted_data.write()

def generate_password():
    pass


# ----- UI SETUP -----
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create canvas widget
canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)

# create the labels
website_label = Label(text="Website:")
email_or_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# create the buttons
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=43, command=add_data)

# create the input entry fields
website_input = Entry(width=50)
email_or_username_input = Entry(width=50)
password_input = Entry(width=32)

# position the widgets
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2)
email_or_username_label.grid(row=2, column=0)
email_or_username_input.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
generate_button.grid(row=3, column=2)
password_input.grid(row=3, column=1)
add_button.grid(row=4, column=1, columnspan=2)

# add text cursor to website entry field
website_input.focus()

# insert a string to the email entry field
email_or_username_input.insert(0, "ahmadkhairi_hamzah85@yahoo.com")

window.mainloop()