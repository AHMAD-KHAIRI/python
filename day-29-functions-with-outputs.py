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
    # print(f_name.title())
    # print(l_name.title())
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f"{formatted_f_name} {formatted_l_name}")
    # instead of print, we can also return an output
    return f"{formatted_f_name} {formatted_l_name}"

# print(format_name("ahmad khairi", "bin hamzah"))
# or we can do this:
formatted_string = format_name("ahmad khairi", "bin hamzah")
print(formatted_string)

# Example of other functions which returns outputs
str_length = len(formatted_string)
print(str_length)