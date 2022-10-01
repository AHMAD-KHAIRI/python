# 68. How to break a complex problem down into a flow chart
# Coded on 29.09.2022
# Hangman coding challenge
import random

# word_list = ["aardvark", "baboon", "camel"]

# Update the word_list to use the 'word_list' from day24HangmanWords.py
# import day24HangmanWords
from day24HangmanWords import word_list
# chosen_word = random.choice(word_list)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# print(chosen_word)

end_of_game = False
lives = 6

# print("Welcome to Hangman!")

# Import the logo from day24HangmanArt.py and print it at the start of the game.
# import day24HangmanArt
from day24HangmanArt import logo, stages
print(logo)

# Create blanks
display = []
  
for letter in chosen_word:
    display += "_"
# print(display)

while not end_of_game:
        guess = input("Guess a letter: ").lower()
        
        if guess in display:
            print(f"You've already guessed {letter}")

        # Check guesses letter
        for position in range(word_length):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter

        print(display)

        # Check if user guess is wrong
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You are out of guesses. The word is {chosen_word}. You Lose!")
        
        # Check if user has guessed all letters
        if "_" not in display:
            end_of_game = True
            print(f"You guessed {chosen_word}. You Win!")

        print(stages[lives])