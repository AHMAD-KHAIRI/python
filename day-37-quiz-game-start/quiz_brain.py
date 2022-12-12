# Task 1: Asking the questions
# Task 2: Checking if the answer is correct
# Task 3: Checking if we're at the end of the quiz

# First create a class called QuizBrain
class QuizBrain:

    # Write an __init__() method
    def __init__(self, q_list):
        # Initialize the question_number to 0
        self.question_number = 0
        # Initialize the question_list to an input
        self.question_list = q_list
        # Initialize the score
        self.score = 0

    # Create a new method called still_has_questions
    def still_has_questions(self):
        # # Returns a boolean depending on the value of question_number
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     False
        # simplify the code above
        return self.question_number < len(self.question_list)

    # Create a next_question() method
    def next_question(self, ):
        # Retrieve the item at the current question_number from the question_list and save in the variable current_question
        current_question = self.question_list[self.question_number]
        # increase question number every time next question is called
        self.question_number += 1
        # Use the input() function to show the user the Question text and ask for the user's answer
        # to check the answer, save the input to a variable called user_answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # Create a new method called check_answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        # Add a blank line 
        print("\n")