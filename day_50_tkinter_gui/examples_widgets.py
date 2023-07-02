# import tkinter
# use the * to import all the classes
from tkinter import *

# by importing all the class, we can remove the module name
window = Tk()
# window = tkinter.Tk()
window.title("My First GUI Program.")
window.minsize(width= 500, height=500)

# Create a label widget
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

# Setting options to configure, update or change the properties
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# Create a button widget
def button_clicked():
    print("I got clicked")
    # my_label["text"] = "Button got clicked"
    new_text = my_input.get()
    my_label["text"] = new_text

my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()

# Create a text input field element widget using Entry()
my_input = Entry(width=30)
my_input.pack()
# returns the input as a string using get()
print(my_input.get())

# Create a text box widget(height refers to no of lines)
my_text_box = Text(width=30, height=5)
my_text_box.focus()
my_text_box.insert(END, "Example of multi-line text entry.")
print(my_text_box.get("1.0", END))
my_text_box.pack()

# Create a spinbox widget
def spinbox_used():
    print(my_spinbox.get())

my_spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
my_spinbox.pack()

# Create a scale widget
def scale_used(value):
    print(value)

my_scale = Scale(from_=0, to=100, command=scale_used)
my_scale.pack()

# Create a checkbutton widget
def checkbutton_used():
    print(checkbutton_state.get())

checkbutton_state = IntVar()
my_checkbutton = Checkbutton(text="Do you agree?", variable=checkbutton_state, command=checkbutton_used)
checkbutton_state.get()
my_checkbutton.pack()

# Create a radiobutton widget
def radiobutton_used():
    print(radiobutton_state.get())

radiobutton_state = IntVar()
my_radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radiobutton_state, command=radiobutton_used)
my_radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radiobutton_state, command=radiobutton_used)
my_radiobutton1.pack()
my_radiobutton2.pack()

# Create a listbox widget
def listbox_used(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox(height=4)
# to list something in the listbox
fruits = ["Apple", "Pear", "Orange", "Kiwi"]
for item in fruits:
    my_listbox.insert(fruits.index(item), item)

my_listbox.bind("<<ListboxSelect>>", listbox_used)    
my_listbox.pack()

# to keep the window open. must be at the end of the code
window.mainloop()