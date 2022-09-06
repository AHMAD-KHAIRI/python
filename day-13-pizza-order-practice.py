# Exercise 4 - Pizza order practice
# Coded on 06.09.2022

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Extras:
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

bill = 0
small = 15
medium = 20
large = 25

# Prepare the flow chart

# 1st condition: size
# if user inputs S then bill is $15
if size == 'S':
    bill = bill + small
    print(bill)

elif size == 'M':
    bill = bill + medium
    print(bill)

elif size == 'L':
    bill = bill + large
    print(bill)
    
# 2nd condition: add pepperoni
if (size == 'S') & (add_pepperoni == 'Y'):
    bill += 2
    print(bill)

if (size == 'M') | (size == 'L'):
    if add_pepperoni == 'Y':
        bill += 3
        print(bill)

elif add_pepperoni == 'N':
    bill
    print(bill)

# 3rd condition: extra cheese
if extra_cheese == 'Y':
    bill += 1
    print(bill)
        
elif extra_cheese == 'N':
    bill
    print(bill)


# 4th condition: print final bill
print(f"Your final bill is: ${bill}.")
