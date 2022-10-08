# 83. Paint Area Calculator
# Coded on 08.10.2022

#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    # number of cans = (wall height * wall width) ÷ coverage per can
    number_of_cans = (test_h * test_w) / coverage
    # math.ceil(x): Return the ceiling of x, the smallest integer greater than or equal to x.
    round_up_number = math.ceil(number_of_cans)
    print(f"You'll need {round_up_number} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

