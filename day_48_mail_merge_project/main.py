# this is the string that we want to replace in our letter
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    # readlines() method returns a list containing each line in the file as a list item
    names = names_file.readlines()
    # read() will opens and reads the content of the file in its original form
    # names = names_file.read()
    # print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    # go through the letter contents and replace the PLACEHOLDER with the names in the names file
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)
        
        # creates new letter for every name and write the content of the letter
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)