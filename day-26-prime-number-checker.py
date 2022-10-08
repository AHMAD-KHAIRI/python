# 84. Prime Number Checker
# Coded on 08.10.2022

# Prime number: Number only divisible by 1 and itself

#Write your code below this line 👇
import math

def prime_checker(number):
    is_prime = True
    for n in range (2, number):
        # print(f"{number} % {n} = {number % n}")
        if number % n == 0:
            # Not a prime number
            is_prime = False
    # If number is a prime
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
