# # new_dict = {new_key: new_value for item in list}
# # compare with: new_list = [new_item for item in list]
# # new_dict = {new_key: new_value for (key, value) in dict.items()}
# # new_dict = {new_key: new_value for (key, value) in dict.items() if test}
# # compare to list comprehension: new_list = [new_item for item in list if test]

# # Examples:
# import random

# names = ["Ahmad", "Khairi", "Iman", "Ezra", "Khayr"]

# # Create a dict with random scores
# # new_dict = {new_key: new_value for item in list}
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)

# # new_dict = {new_key: new_value for (key, value) in dict.items() if test}
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)


# # Exercise 1:
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# sentence_list = sentence.split()

# result = {letter:len(letter) for letter in sentence_list}

# print(result)

# # Exercise 2:
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆


# # Write your code 👇 below:
# weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}


# print(weather_f)

# # new_list = [new_item for item in list if test]
# # new_dict = {new_key:new_value for item in list}
# # new_dict = {new_key:new_value for (key, value) in list if dict.items() if test}


# How to iterate over Pandas DataFrame
student_dict = {
    "student": ["Ahmad", "Khairi", "Iman", "Ezra"],
    "score": [56, 76, 86, 98]
}

# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# pandas in-built loop using iterrows() method
for (index, row) in student_dataframe.iterrows():
    print(row.student)
    print(row.score)