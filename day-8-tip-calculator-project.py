# Coded on 29.08.2022

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# print("Welcome to the tip calculator!")

# total_bill = input("What was the total bill? $")

# tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

# total_split = input("How many people to split the bill? ")

# bill_per_person = float(total_bill) / int(total_split) * (1 + int(tip_percentage) / 100)

# print(f"Each person should pay: ${round(bill_per_person, 2)}")


# Solution from udemy:
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_Bill = bill + total_tip_amount
bill_per_Person = total_Bill / people
# final_amount = round(bill_per_Person, 2)
# instead of using round due to python formatting issue, we use format function as below:
final_amount = "{:.2f}".format(bill_per_Person)

print(f"Each person should pay: ${final_amount}")