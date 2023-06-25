
# we can use the method open to open, read, close a file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# a different way is to use "with" keyword
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# to write to a file, change mode to "w" (write). ** It will delete all the content previously saved
# with open("my_file.txt", mode="w") as file:
    # file.write("New text.")

# to write to a file but not deleting previous content, change mode to "a" (append)
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# if the file is not crated, using mode "w" will create the new file
with open("new_file.txt", mode="w") as file:
    file.write("New text.")