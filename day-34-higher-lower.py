# import day34HigherLowerArt
# import day34HigherLowerGameData
# import random

# print(day34HigherLowerArt.logo)
# print(f"Compare A: ")
# print(day34HigherLowerGameData.data[1])
# print(day34HigherLowerArt.vs)
# print(f"Against B: ")
# user_choice = input("Who has more followers? Type 'A' or 'B': ")

# ------------------------------------------------------------------------------------------------------

# Format the account data into printable format (turn into a function)
def format_data(account):
    """ Takes the account data and returns the printable format. """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """ Take the user guess and follower counts and returns if user is correct. """
    # Option A:
    # if a_followers > b_followers:
        # if guess == "a":
            # return True
        # else:
            # return False
    # Option B:
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
from day34HigherLowerArt import logo, vs
print(logo)

# Generate a random account from the game
from day34HigherLowerGameData import data
import random

# Score keeping
score = 0

# Make the game repeatable
game_should_continue = True
while game_should_continue:

    account_a = random.choice(data)
    account_b = random.choice(data)
    # # Check data from account_a and account_b is the same. If yes, regenerate
    if account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format (moved to function format_data)
    # account_name = account_a["name"]
    # account_desc = account_a["description"]
    # account_country = account_a["country"]
    # print(f"{account_name}, a {account_desc}, from {account_country}")
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check is user is correct 
    # # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # # Use if statement to check if user is correct (use function check_answer)
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        # Stop the game if guess is wrong. End the while loop
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")


    # Making account at position B become the next account at position A

    # Clear the screen between rounds