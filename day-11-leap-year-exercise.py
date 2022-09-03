# Exercise 3 - Leap Year
# Coded on 03.09.2022

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Prepare a flow chart:

# 1st: If the year is divided by 4, is it evenly divided (that means without a remainder?
# If Yes, then proceed down
# If No, then print "Not leap year."

# 2nd: If the year is divided by 100, is it evenly divided?
# If Yes, then proceed down
# If No, then print "Leap year."

# 2rd: If the year is divided by 400, is it evenly divided?
# If yes, then print "Leap year."
# If No, then print "Not leap year."

# My solution:
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    else:    
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")    
else:
    print("Not leap year.")


# print(f"{year} divided by 4 is {year / 4} and the remainder is {year % 4}.")
# print(f"{year} divided by 100 is {year / 100} and the remainder is {year % 100}.")
# print(f"{year} divided by 400 is {year / 400} and the remainder is {year % 400}.")

# Udemy trainer solution:
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")    

