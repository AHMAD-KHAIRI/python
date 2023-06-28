with open("file1.txt") as file_1:
    new_file_1 = file_1.readlines()

with open("file2.txt") as file_2:
    new_file_2 = file_2.readlines()

result = [int(n) for n in new_file_1 if n in new_file_2]

# Write your code above 👆

print(result)