3 + 5
7 - 4
3 * 2
6 / 3
# division outputs a float data type
print(type(6 / 3))
2 ** 3

# PEMDAS / BODMAS rule in mathematics
# executed from Left to Right (l2R)
# () Parentheses / Bracket
# ** Exponents / Order 
# * Multiplication and / Division
# + Addition 
# - Subtraction

# example:
print(3 * 3 + 3 / 3 - 3)
# first order: 3 * 3 = 9 
# second order: 3 / 3 = 1
# third order: 9 + 1 = 10
# fourth order: 10 - 3 = 7 --> output

# challenge: change the result of the math operation above to 3.0
print(3 * (3 + 3) / 3 - 3)
# (3 + 3) = 6
# 3 * 6 = 18
# 18 / 3 = 6
# 6 - 3 = 3

# Day 2 / Exercise 2 - BMI Calculator
# Coded on 27.08.2022

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(type(height), type(weight)) --> type str

# from the user input, convert height and weight from str to float data type
height_conv_to_float = float(height)

weight_conv_to_float = float(weight)

# calculate the height squared and save it in a variable
height_squared = height_conv_to_float ** 2

# print(type(height_conv_to_float), type(weight_conv_to_float))

# here are multiple ways to do the mathematics calculation to get the bmi result:
# bmi_result_float = weight_conv_to_float / (height_conv_to_float * height_conv_to_float)
# bmi_result_float = weight_conv_to_float / (height_conv_to_float ** 2)
bmi_result_float = weight_conv_to_float / (height_squared)

# print(result_float)

# print out the bmi calculation formula and the results
print(weight, "÷ (", height, " x ", height, ") = ", bmi_result_float)

# convert the bmi result from float to int data type
bmi_result_int = int(bmi_result_float)

# display the bmi results in int data type
print(bmi_result_int)


# solution from udemy trainer
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)




