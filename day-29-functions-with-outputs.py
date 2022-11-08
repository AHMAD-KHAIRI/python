# 99. Functions with Outputs
# Coded on 29.10.2022

# recap on function:
# 1. Basic function
# first define a function
# def my_function():
    # Do this
    # Then do this
    # Finally do this
# next, call up the function
# my_function()
# 2. Function with inputs
# def my_function(something): where something is the parameter
    # Do this with something
    # Then do this
    # Finally do this
# my_function(123) where 123 is the argument which gets passed in the parameter

# 3. Functions with outputs
# def my_function():
#     result = 3 * 2
#     return result
    # or simply can be written:
    # return 3 * 2

# Assign the output of the function: my_function() to a variable
# output = my_function()

# Example: 
# How to format a string where words start with an uppercase character and the remaining characters are lowercase
# use the method title()
def format_name(f_name, l_name):
    # Docstrings (""" """) are a documenting feature for multi-line comment that provides an overview of the function description
    """ Take a first and last name and format it to return the title case version of the name."""
    # multiple return values:
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f"{formatted_f_name} {formatted_l_name}")
    # instead of print, we can also return an output
    return f"{formatted_f_name} {formatted_l_name}"

# print(format_name("ahmad khairi", "bin hamzah"))
# or we can do this:
formatted_string = format_name(input("What is your first name? "), input("What is your last name? "))
# formatted_string = format_name("ahmad khairi", "bin hamzah")
print(formatted_string)

# Example of other functions which returns outputs
# str_length = len(formatted_string)
# print(str_length)


# 101. Days in Month coding challenge
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)