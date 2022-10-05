# 80. Day 8 
# Coded on 05.10.2022

# Build a cipher program "Caesar Cipher"

# Review:
# Create a function called greet()
# Write 2 print statements inside the function
# Call the greet() function and run your code

def greet():
    print("Good Morning AK!")
    print("Happy Programming!")
    print("Don't Give Up!")

greet()

# functions with inputs
# def my_function(something): where something is called the Parameter-the name of data that is being passed in
    # Do this with something
    # Then do this
    # Finally do this

# my_function(123) where 123 is called the Argument-the actual value of the data


# Function that allows for input
# def greet_with_name(name):
#     print(f"Good Morning {name}!")
#     print("Happy Programming!")
#     print("Don't Give Up!")

# greet_with_name("Khairi")


# 82. Positional vs Keyword Arguments
# Coded on 05.10.2022

# Function with more than 1 inputs
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Khairi", "Malaysia")

# what if we switch the order of the parameter?
# greet_with("Malaysia", "Khairi") # output: Hello Malaysia, What is it like in Khairi?

# Positional Arguments
# def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this witch c

# my_function(1, 2, 3)
# where a = 1, b = 2, c = 3

# my_function(3, 1, 2)
# where a = 3, b = 1, c = 2

# Instead we can use Keyword Arguments
# def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this witch c

# my_function(a=1, b=2, c=3)
# my_function(c=3, b=2, a=1)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(name="Khairi", location="Malaysia")