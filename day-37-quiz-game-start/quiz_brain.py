# Task 1: Asking the questions
# Task 2: Checking if the answer is correct
# Task 3: Checking if we're at the end of the quiz

# First create a class called QuizBrain
class QuizBrain:

    # Write an __init__() method
    def __init__(self, q_list):
        # Initialize the question_number to 0
        self.question_number = 0
        # Initialize the question_list to an inpur
        self.question_list = q_list

    # Create a next_question() method
    def next_question(self, ):
        # Retrieve the item at the current question_number from the question_list and save in the variable current_question
        current_question = self.question_list[self.question_number]
        # increase question number every time next question is called
        self.question_number += 1
        # Use the input() function to show the user the Question text and ask for the user's answer
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
