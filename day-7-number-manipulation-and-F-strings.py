# 24. Number manipulation and F Strings in Python
# Coded on 28.08.2022

# normal mathematic calculation prints out results in float data type
print(8 / 3)

# to print out results in int data type, we need to convert them to int
print(int(8 / 3))

# to round numbers
print(round(8 / 3))

# specify the no of digits (ndigits) precision to round it to
print(round(8 / 3, 2))

# use "//" (floor division) so that we don't get the results as float data type
# and without converting it to int data type
print(round(8 // 3))
print(type(round(8 // 3)))

# if we save the result of the calculation in a variable, we can reuse again for the next calculation
result = 4 / 2
result /= 2
# result = result / 2
print(result)

# another example:
score = 0
height = 1.8
isWinning = True

# User scores a point
score += 1
# score -= 1
# score *= 1
# score /= 1

print(score)


# F Strings: Mix strings and different data type
# print("Your score is " + score) --> will cause a TypeError

# To solve this, we need to convert to str in order to concatenate using '+' sign
print("Your score is " + str(score))

# To make it even easier/convenient, we can use F Strings and call up variables inside the curly braces {}
print(f"Your score is {score}, height is {height} and you are winning is {isWinning}")


# Coding Challenge: Exercise 3 - Life in Weeks

# Create a program using maths and f-Strings that tells us # how many days, 
# weeks, months we have left if we live until 90 years old

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# 1 year = 365 days, 1 year = 52 weeks, 1 year = 12 months
# Desired output: You have x days, y weeks, and z months left.

# total_days_to_live = (90 - int(age)) * 365
# total_weeks_to_live = (90 - int(age)) * 52
# total_months_to_live = (90 - int(age)) * 12
# print(f"You have {total_days_to_live} days, {total_weeks_to_live} weeks, and {total_months_to_live} months left.")


# Solution from udemy:

# first convert age into int data type
age_as_int = int(age)

# second calculate the mathematics
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

# check if answer is correct
print(days_remaining, weeks_remaining, months_remaining)

# print results and save in a variable
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)


# Quiz 4: Mathematical Operations Quiz

# Question 1: What is the output?
print(6 + 4 / 2 - (1 * 2))
# first brackets: 1 * 2 = 2
# second division: 4 / 2 = 2
# third addition: 6 + 2 = 8
# fourth subtraction: 8 - 2 = 6 --> Output/Result

# Question 2: What is the data type of the variable a?
a = int("5") / int(2.7)
print(type(a))
# output: float
# Reason: any numbers which uses a division, will get the result in float data type
# By using floor division //, we will get int data type

x = int("5")
y = int(2.7)
z = x / y
z1 = x // y
print(z, type(z), z1, type(z1))

# Question 3: Which will produce a TypeError
# Solution: D --> We cannot concatenate strings with int data type, hence need to convert to str first OR use f-strings