# 31. Nested if and elif statements
# Coded on 01.09.2022
# if condition:
#   if another condition:
#       do this
#   elif another condition:
#       do this
#   else:
#       do this
# else:
#   do this

# From Exercise #1: Rollercoaster ride height
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Check if the height is greater than 120cm to play the rollercoaster
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    # Check if age is less than or equal to 18 and pay $7
    elif age <= 18:
        print("Please pay $7.")
    # If age is above 18, then pay $12
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to be taller than 120cm to ride the rollercoaster! ")