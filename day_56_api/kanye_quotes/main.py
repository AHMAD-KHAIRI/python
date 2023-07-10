from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 212, image=background_image)
canvas.grid(row=0, column=0)

kanye_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_image, command=get_quote)
kanye_button.grid(row=1, column=0)

quote_text = canvas.create_text(150, 212, text="Kanye Quote Goes HERE", fill="white", width=250, font=("Arial", 22, "bold"))

window.mainloop()