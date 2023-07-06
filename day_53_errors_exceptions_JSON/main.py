# Types of errors commonly found:

# FileNotFound
# with open("a_file.txt") as file:
    # file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Orange", "Pear"]
# fruit_list[3]

# TypeError
# text = "Abc"
# text + 5


# In programming, we can catch exceptions using these keywords
# try: use this block of code for something that might cause an exception / if this fails then go to exception
# except: do this block of code if there was an exception
# else: do this block of code if there were no exceptions
# finally: do this block of code no matter what happens / don't care

# FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["non_existent_key"]

# except:
# except code block cannot be bare (aka broadscope) because it will not catch other types of error
    # print("there was an error")
    # file = open("a_file.txt", "w")
except FileNotFoundError:
# only when we specify the exception that the except code block can catch other types of errors such as KeyError
    file = open("a_file.txt", "w")
    file.write("something")
# we can have more than 1 exception code of block
# except KeyError:
    # print("That key does not exist.")
# we can also catch the error message
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    # file.close()
    # print("File was closed.")
    raise TypeError("This is an error that I made up.")

# when do we want to "raise" an error? Example below
height = float(input("Height: "))
weight = int(input("Weight: "))

# if the user enters a ridiculous value such as height = 45m, we can raise an error
if height > 3:
    raise ValueError("Human height should not be more than 3m.")

bmi = weight / height ** 2
print(bmi)