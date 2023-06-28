# # How it started:
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)


# # there's also an inbuilt library with CSV
# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)


# # Pandas - Python data analysis library working with CSV data
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# # A DataFrame in Pandas is like a whole table

# temperatures = data["temp"]
# print(type(temperatures))
# # print(temperatures)
# # A Series in Pandas is equivalent to a list

# # Convert the DataFrame to a dictionary using pandas.DataFrame.to_dict
# data_dict = data.to_dict()
# print(data_dict)

# # Convert the Series object to a list using pandas.Series.to_list()
# temp_list = temperatures.to_list()
# print(temp_list)

# # calculate average temperature
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# # alternatively using pandas.Series.mean()
# average = temperatures.mean()
# print(average)

# # find the max temp, hint: use pandas.Series.max()
# max_temp = temperatures.max()
# print(max_temp)

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get data in rows
# print(data[data.day == "Monday"])

# # Find the row of data where the temp is the highest
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = int(monday.temp)
# print(monday_temp * 9/5 + 32)

# # Create a Pandas DataFrame from scratch
# students_data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(students_data_dict)
# print(new_data)
# # convert to csv:
# new_data.to_csv("new_data.csv")


# Analyze the 2018 central park squirrel data
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")

# Filter out squirrels based on fur color
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

# Calculate total squirrels for each fur color
grey_squirrels_count = len(grey_squirrels)
red_squirrels_count = len(red_squirrels)
black_squirrels_count = len(black_squirrels)
print(grey_squirrels_count, red_squirrels_count, black_squirrels_count)

# Create a new dataframe and convert to csv
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")