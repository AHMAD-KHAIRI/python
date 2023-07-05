# ----- IMPORT LIBRARIES -----
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ----- FUNCTIONS -----
# SAVE THE DATA MECHANISM
def save_data():
    website = website_input.get()
    email = email_or_username_input.get()
    password = password_input.get()

    # do a validation check if the fields are left empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else: 
        print(website, email, password)
        # opens a popup message box after the add button is pressed
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
        # if ok button is pressed
            # everytime the add button is pressed, append/insert new data into file data.txt
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")  
                # clears the entry fields after the add button is pressed
                website_input.delete(0, END)
                password_input.delete(0, END)

# GENERATE RANDOM PASSWORD MECHANISM
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(nr_letters):
        # password_list.append(random.choice(letters))

    # for sym in range(nr_symbols):
        # password_list.append(random.choice(symbols))

    # for num in range(nr_numbers):
        # password_list.append(random.choice(numbers))

    # convert the for loop to list comprehension:
    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # for char in random_password:
        # password += char
    # replace the for loop with join() method
    password = "".join(password_list)

    # insert the randomly generated password into the password entry field
    password_input.insert(0, password)

    # insert pyperclip copy method to automatically copy the password into clipboard
    pyperclip.copy(password)


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

# pre-insert a string to the email entry field
email_or_username_input.insert(0, "ahmadkhairi_hamzah85@yahoo.com")

# keep the window open
window.mainloop()