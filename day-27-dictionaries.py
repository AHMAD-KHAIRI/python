# 91. The Python dictionary: Deep Dive
# Coded on 24.10.2022
# Dictionary in python is similar to dictionary in real life
# For example if we want to find the definition of a word in the dictionary
# The word that we want to look up for is the "key", while the definition is the "Value"
# To create a dictionary, the basic syntax: {key: Value}
# {"Bug": "An error in a program that prevent the program from running as expected."}

# If more than 1 entry in the dictionary, we use comma to separate the entries:
# {
#     "Bug": "An error in a program that prevent the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."
# }

# A dictionary can be stored in a variable:
programming_dictionary = {
    "Bug": "An error in a program that prevent the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# To retrieve an item in a dictionary:
print(programming_dictionary["Bug"])

# Adding a new item into the dictionary:
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Same way as we create an empty list, we can do the same with dictionary:
empty_list = []
empty_dictionary = {}

# Wipe an existing dictionary:
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# 92. Interactive Coding Exercise
# Day 9 / Exercise 1 - Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# This is the scoring criteria:
#     Scores 91 - 100: Grade = "Outstanding"
#     Scores 81 - 90: Grade = "Exceeds Expectations"
#     Scores 71 - 80: Grade = "Acceptable"
#     Scores 70 or lower: Grade = "Fail"
# my_solution:
# for key in student_scores:
#     if student_scores[key] > 90:
#         student_scores[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_scores[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70:
#         student_scores[key] = "Acceptable"
#     else:
#         student_scores[key] = "Fail"
#     student_grades[key] = student_scores[key]

# udemy solution:
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# 93. Nesting Lists and Dictionaries

# A dictionary looks like this: {Key: Value} where each Key contains one Value
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# A dictionary with a nested list and dictionary looks like this:
# {
# Key: Value1,
# Key2: [List],
# Key3: {Dict},
# }

# Nesting a list in a Dictionary:
travel_log = {
    "France": ["Paris", "Nice", "Monaco"],
    "Germany": ["Berlin", "Frankfurt", "Munich", "Stuttgart", "Wurzburg", "Ulm"],
}

# Nesting a list in a list is not quite useful compared to a nested dictionary:
# ["A", "B", ["C", "D"]]

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {
        "cities_visited": [
            "Paris", 
            "Nice", 
            "Monaco"], 
        "total_visits": 12
        },
    "Germany": {
        "cities_visited": [
            "Berlin", 
            "Frankfurt", 
            "Munich", 
            "Stuttgart", 
            "Wurzburg", 
            "Ulm"],
        "total_visits": 24
    },
}

# Nesting a Dictionary in a List
# [{
#     Key: [List],
#     Key2: {Dict},
# },
# {
#     Key: Value,
#     Key2: Value,
# }]
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Nice", "Monaco"], 
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Frankfurt", "Munich", "Stuttgart", "Wurzburg", "Ulm"],
        "total_visits": 24
    },
]

# Exercise 2 - Dictionary in List
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, num_of_visits, cities_visited):
    # first create an empty dictionary
    new_country = {}
    # secondly, assign the key with the function parameters
    new_country["country"] = country_visited
    new_country["visits"] = num_of_visits
    new_country["cities"] = cities_visited
    # finally, to add an item to an existing list, we can use append()
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
