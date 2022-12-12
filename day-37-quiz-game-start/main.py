from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Task 1: Write a for loop to iterate over the question_data
# First create an empty list and save in question_bank variable
question_bank = []
# Second, loop through each of the questions inside question_data using a for loop
for question in question_data:
    # Third, for each question, create a variable to hold the data inside question_data
    # question_text = question["text"]
    # question_answer = question["answer"]
    # format according to new question_data from opentdb
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Task 2: Create a new_question object from our Question class and link the data inside question_data
    # new_question = Question(inputs)
    new_question = Question(question_text, question_answer)
    # Task 3: Append each Question object to the question_bank
    question_bank.append(new_question)

# # Testing Task 1 - 3
# print(question_bank)
# print(len(question_bank))
# print(question_bank[0].text)
# print(question_bank[0].answer)


# initialize QuizBrain 
quiz = QuizBrain(question_bank)

# Create a while loop to keep asking next_question if the question_bank still_has_questions
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")