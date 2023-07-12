import html

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
        return self.question_number < len(self.question_list)

    # Create a next_question() method
    def next_question(self):
        # Retrieve the item at the current question_number from the question_list and save in the variable current_question
        self.current_question = self.question_list[self.question_number]
        # increase question number every time next question is called
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    # Create a new method called check_answer
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False