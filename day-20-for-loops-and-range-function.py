# 53. for loops and range() function
# Coded on 20.09.2022

# for loop with range:

# for number in range(a, b):
    # print(number)

# prints 1,2,3,4,5,6,7,8,9
# for number in range(1, 10):
    # print(number)

# prints 1,2,3,4,5,6,7,8,9,10
# for number in range(1, 11):
    # print(number)

# By default the range will step through the numbers from start to the end and increase by 1
# To increase by any other number, add another comma to the end of the range and specify how large the step to be
# For example, step increase by 3
# prints 1, 4, 7, 10
# for number in range(1, 11, 3):
    # print(number)
# range(start, end, step)

# How can we add up number 1 to 100 using for loop with range
# total = 0
# for number in range(1, 101):
#     total += number

# print(total)


# 54. Coding Exercise 3 - Adding Even Numbers

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. 
# It should just print the final total and not every step of the calculation.
# Hint
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.


#Write your code below this row 👇

from calendar import c


total_even_numbers = 0

for number in range(0, 101, 2):
    total_even_numbers += number

print(total_even_numbers)


# Udemy trainer solution:

total = 0
for number in range(2,101, 2):
    total += number
print(total)

# Another way to do this:
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)


# 55. Coding Exercise 4 - FizzBuzz
# Instructions

# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# Hint
# 1. Remember your answer should start from 1 and go up to and including 100.
# 2. Each number/text should be printed on a separate line.

#Write your code below this row 👇

for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        if number % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(number)