# 24082022 @ 10.30 PM
# len function doesn't accepts int and will output type error
# len(1234)

# num_char = len(input("What is your name?"))

# print(type(num_char))

# convert data type to str
# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")
# the above will get a type error because concat "+" can only be done with strings and not int
# one solution is to convert to string with str()

# another solution is to use below:
# print(f"Your name has {num_char} characters.")

# other examples of data type conversions:
# a = str(123)
# a = float(123)
# print(type(a))

# print(70 + float("100.50"))
# print(str(70) + str(100.50))

# ==================================================================================================
# Day 2 - Exercise 1 - Data Types
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
# print(type(first_digit))
# print(type(second_digit))
print(first_digit + second_digit)