# This is how we normally do with a list
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# List Comprehension
# new_numbers = [new_item for item in list] --> using keywords
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Khairi"
letters_list = [letter for letter in name]
print(letters_list)

# list, range, tuple, string are called Python sequences

new_range = []
for n in range(1, 5):
    double = n * 2
    new_range.append(double)
print(new_range)

range_list = [n * 2 for n in range(1,5)]
print(range_list)


# Conditional List Comprehension
# new_list = [new_item for item in list if test]
# Example:
names = ["Ahmad", "Khairi", "Iman", "Ezra", "Khayr"]
# create a list of short names with less than 5 chars
short_names = [name for name in names if len(name) < 5]
print(short_names)

# create a list of names with more than 5 chars and convert to uppercase
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)