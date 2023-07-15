# Write, read, and update JSON data in password manager
# To work with JSON data in python, we can use the json library
# To write, use: json.dump() and mode="w"
# To read, use: json.load() and mode="r"
# To update, use: json.update() --> 3 step approach: read, update and dump
# Here is how our new data.json will look like:
# {
#     "Amazon" : {
#         "email": "khairi@gmail.com",
#         "password": "abc123"
#     },
#     "Youtube" : {
#         "email": "khairi@gmail.com",
#         "password": "def456"
#     },
#     "Github" : {
#         "email": "khairi@gmail.com",
#         "password": "ghi789"
#     }
# }


# ----- IMPORT LIBRARIES -----
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ----- FUNCTIONS -----
# SAVE THE DATA MECHANISM
def save_data():
    website = website_input.get()
    email = email_or_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
                }

    # do a validation check if the fields are left empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else: 
        # with exception handling using try, except, else and finally
        try: 
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
        
        # without exception handling
        # with open("data.json", mode="r") as data_file:
            # To write, use json.dump() and mode="w"
            # json.dump(new_data, data_file, indent=4)

            # To read, use json.load() and mode="r"
            # data = json.load(data_file)
            # print(data)

            # To update, use json.update() and 3 step approach:
            # 1. Read old date
            # data = json.load(data_file)
            # 2. Update old data with new data
            # data.update(new_data)
        
        # with open("data.json", mode="w") as data_file:
        #     # 3. Save updated data
        #     json.dump(data, data_file, indent=4)

            # clears the entry fields after the add button is pressed
            # website_input.delete(0, END)
            # password_input.delete(0, END)

# GENERATE RANDOM PASSWORD MECHANISM
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)

# FIND PASSWORD MECHANISM (with exception handling)
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    # catch exception when no data.json file exists
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file is found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



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
add_button = Button(text="Add", width=43, command=save_data)
# added Search button for challenge 2
search_button = Button(text="Search", width=15, command=find_password)

# create the input entry fields
website_input = Entry(width=32)
email_or_username_input = Entry(width=50)
password_input = Entry(width=32)

# position the widgets
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1)
search_button.grid(row=1, column=2)
email_or_username_label.grid(row=2, column=0)
email_or_username_input.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
generate_button.grid(row=3, column=2)
password_input.grid(row=3, column=1)
add_button.grid(row=4, column=1, columnspan=2)

# add text cursor to website entry field
website_input.focus()

# pre-insert a string to the email entry field
email_or_username_input.insert(0, "ak.test.smtp.python@gmail.com")

# keep the window open
window.mainloop()