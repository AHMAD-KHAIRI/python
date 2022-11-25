############DEBUGGING#####################

# # Describe Problem: for loop stops at 19 hence if statement will not get true. 
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
# Solution: change 20 to 21

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
# # solution: change the range

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# Solution: add >= to elif statement

## Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
    # print(f"You can drive at age {age}.")
# solution: add indent, convert input str to int, add f string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # solution: remove "=" from word_per_page

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
# solution: add indent to line b_list.append(new_item)