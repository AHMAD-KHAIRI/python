# First task: create a Class called Question, create two attributes called text and answer and then initialize them
class Question:
    # create two attributes called text and answer and initialize them
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# # testing the first task
# new_q = Question("First question", "True")
# print(new_q.text)
# print(new_q.answer)

# Second task: Create a question_bank