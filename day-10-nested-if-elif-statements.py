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


# Exercise 2 - BMI 2.0
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")