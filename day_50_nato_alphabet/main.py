import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Step 1: Create a dictionary
# new_dict = {new_key:new_value for (index, row) in df.iterrows()}
new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(new_dict)

# Step 2: Asks user to input the name
# word = input("Enter a word: ").upper()

# new_list = [new_item for item in list]
# new_list = [new_dict[letter] for letter in word]
# print(new_list)

# Challenge: Amend the code to add exception handling
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        new_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_list)

generate_phonetic()