# 116. Namespaces: Local vs Global scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}") 
#     # output: enemies inside function: 2

# increase_enemies()
# print(f"enemies outside function: {enemies}")
# # output: enemies inside function: 1

# # Local Scope 
# # exists within a function
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# # output: 2

# # Global scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength) # local scope - defined inside a function
#     print(player_health) # global scope - defined outside a function

# drink_potion()

# # # # # BLOCK SCOPE # # # # #
# In python, there is no Block Scope. Inside a if/else/for/while code block is the same as outside it. 
# Within a function, there is a local scope
# If a variable is created within a function, then it is only available within that function

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy) # output: Skeleton

# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy) # Output: Skeleton
# create_enemy()
# print(new_enemy) # Output: new_enemy is not defined --> variable is not accessible inside a function


# # # # # MODIFYING GLOBAL SCOPE # # # # #

enemies = 1

def increase_enemies():
    # global allows us to access variables outside of the function
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}") 
    # output: enemies inside function: 2

increase_enemies()
print(f"enemies outside function: {enemies}")
# output: enemies inside function: 2


# # # # # GLOBAL CONSTANTS # # # # #
# Naming Convention: All variables use Uppercase Separated with Underscores
PI = 3.14159
URL = "https://www.google.com"
IG_HANDLE = "AHK1KHA"

def calc():
    PI