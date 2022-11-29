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
    """ Format the account data into printable format. """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


# Display art
from day34HigherLowerArt import logo, vs
print(logo)

# Generate a random account from the game
from day34HigherLowerGameData import data
import random
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
user_choice = input("Who has more followers? Type 'A' or 'B': ")

# Check is user is correct
# # Get follower count of each account
# # Use if statement to check if user is correct

# # Give user feedback on their guess

# Score keeping

# Make the game repeatable

# Making account at position B become the next account at position A

# Clear the screen between rounds