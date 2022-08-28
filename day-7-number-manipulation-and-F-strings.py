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
