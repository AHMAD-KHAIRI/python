# 68. How to break a complex problem down into a flow chart
# Coded on 29.09.2022
import random
from turtle import right
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

print("Welcome to Hangman!")
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# Option 1: use random.randint
# num_of_words = len(word_list)
# random_choice = random.randint(0, num_of_words - 1)
# chosen_word = word_list[random_choice]

# Option 2: use random.choice
# chosen_word = random.choice(word_list)
# print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if guess == letter:
#         print("Right")
#     else:
#         print("Wrong")


#Step 2

#TODO-1: - Create an empty List called display.
# display = []
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# for letter in chosen_word:
#     display += "_"
# print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if guess == letter:
#         display[position] = letter


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display)


# Complete Step 1 and Step 2
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
  
for letter in chosen_word:
    display += "_"
print(display)

# guess = input("Guess a letter: ").lower()

# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if guess == letter:
#         display[position] = letter

# print(display)


# Step 3

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# My solution to Step 3
# while not display == list(chosen_word):
    
#     guess = input("Guess a letter: ").lower()

#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if guess == letter:
#             display[position] = letter

#     print(display)

# print("You Win!")

# Udemy trainer's solution to Step 3
end_of_game = False

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")