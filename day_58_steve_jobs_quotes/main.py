from tkinter import *
import requests, random, html, json

def get_quote():
    # source: https://www.invajy.com/steve-jobs-quotes/
    with open("quotes.json", mode="r", encoding="utf8") as quotes_file:
        quotes_data = json.load(quotes_file)
        quote = random.choice(quotes_data["quotes"])
        quote_list = [value for (key, value) in quote.items()]
        canvas.itemconfig(quote_text, text=f"{quote_list[0]}")


window = Tk()
window.title("Steve Jobs says...")
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 212, image=background_image)
canvas.grid(row=0, column=0)

steve_jobs_image = PhotoImage(file="steve-jobs-thumbnail.png", width=250, height=250)
steve_jobs_button = Button(image=steve_jobs_image, command=get_quote, highlightthickness=0)
steve_jobs_button.grid(row=1, column=0)

quote_text = canvas.create_text(150, 212, text="Steve Jobs Quote Goes HERE", fill="white", width=250, font=("Arial", 22, "bold"))

window.mainloop()