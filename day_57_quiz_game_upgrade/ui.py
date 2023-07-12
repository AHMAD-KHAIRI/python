from tkinter import *
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", foreground="white", background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Trivia Questions HERE.", fill=THEME_COLOR, font=("Ariel", 20, "italic"))

        checkmark_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=checkmark_image, highlightthickness=0, command=self.true_button_pressed)

        cross_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=cross_image, highlightthickness=0, command=self.false_button_pressed)

        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        is_true = self.quiz.check_answer("False")
        self.give_feedback(is_true)

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)