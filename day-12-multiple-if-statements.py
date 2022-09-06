# 34. Multiple if statements in Succession
# Coded on 05.09.2022

# Recap:
# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#   do C

# if condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#   do C

# From Exercise #1: Rollercoaster ride height
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0;

# Check if the height is greater than 120cm to play the rollercoaster
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    # Check if age is less than or equal to 18 and pay $7
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    # If age is above 18, then pay $12
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        # Add 3$ to the total bill
        bill += 3
    print(f"Your total bill is ${bill}.")

else:
    print("Sorry, you have to be taller than 120cm to ride the rollercoaster! ")