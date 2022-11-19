# 120. Introducing the Final Project: The Number Guessing Game

import random

# Starting code
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

# User to choose difficulty
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if game_level == "easy":
    score = 10
    print(f"You have {score} attempts remaining to guess the number.")
else:
    score = 5
    print(f"You have {score} attempts remaining to guess the number.")

# random number generator
random_integer = random.randint(1, 100)

# User to guess the number
still_playing = True

while still_playing and score > 0:
    user_guess = int(input("Make a guess: "))
    if user_guess > random_integer and score > 0:
        print("Too high.")
        print("Guess again.")
        score -= 1
        print(f"You have {score} attempts remaining to guess the number.")
    elif user_guess < random_integer and score > 0:
        print("Too low.")
        print("Guess again.")
        score -= 1
        print(f"You have {score} attempts remaining to guess the number.")
    elif user_guess == random_integer and score > 0:
        print(f"You got it! The answer was {random_integer}.")
        print(f"Your score is {score}.")
        still_playing = False

if score == 0:
    print(f"You run out of attempts. Your score is {score}.")
else:
    print("Thanks for playing!")


# Solution from Udemy:
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()