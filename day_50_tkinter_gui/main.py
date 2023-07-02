# =========== import libraries ===========
# import tkinter
# use the * to import all the classes
from tkinter import *
# =======================================


# =========== declare functions ===========
def button_clicked():
    print("I got clicked")
    # my_label["text"] = "Button got clicked"
    new_text = my_input.get()
    my_label["text"] = new_text
# =======================================


# by importing all the class, we can remove the module name
window = Tk()
# window = tkinter.Tk()
window.title("My First GUI Program.")
window.minsize(width= 500, height=500)
# Add padding to all widgets
window.config(padx=20, pady=20)

# Create a label widget
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# Add padding to a widget
my_label.config(padx=20, pady=20)

# Create a button widget
my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

# Create a text input field element widget using Entry()
my_input = Entry(width=10)
my_input.grid(column=3, row=2)
# returns the input as a string using get()
print(my_input.get())


# to keep the window open. must be at the end of the code
window.mainloop()