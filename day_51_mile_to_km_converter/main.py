from tkinter import *

def miles_to_km():
    miles = float(user_input.get())
    km = miles * 1.60934
    result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Cnverter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 20, "normal"))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("Arial", 20, "normal"))
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Arial", 20, "normal"))
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 20, "normal"))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", font=("Arial", 20, "normal"), command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()