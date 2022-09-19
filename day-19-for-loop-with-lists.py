# 50. Using the for loop with Python Lists
# Coded on 19.09.2022

fruits = ["Apples", "Peach", "Pear"]

# To access each item in the list indvidually and print it out one-by-one, we use for loop
for fruit in fruits:
    print(fruit)
# for loop assigns the variable name "fruit" to each of the item in the list
# fruit = Apples then print
# fruit = Peach then print
# fruit = Pear then print

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# indentation after the colon is important
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits)
print(fruits)


# Day 5 Exercise 1 - Average
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Sample input: 150 160 170 155 165 175
# Do not use sum() and len() like commented below:
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)

print(student_heights)

# using for loop to calculate sum()
total_height = 0

for height in student_heights:
    total_height += height
    
print(total_height)

# using for luup to calculate len()
number_of_students = 0

for student in student_heights:
    number_of_students += 1

print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)


# Day 5 Exercise 2 - High Score
# Sample input: 78 65 89 86 55 91 64 89
# Do not use max() or min() functions below:
# highest_score = max(student_scores)
# lowest_score = min(student_scores)

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")