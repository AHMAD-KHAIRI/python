
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resource_sufficient(order_ingredients):
    """ Returns True when ingredients are sufficient to make a drink, False if ingredients are insufficient. """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """ Returns the total amount from coins inserted. """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """ Returns True when payment is accepted, False when money is insufficient. """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"You've paid $ {money_received}. Here is $ {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"You've paid $ {money_received}. Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from resources to make the drink. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice}. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: $ {profit}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        print(f"The price of your {choice} is {drink['cost']}")
        if is_resource_sufficient(drink["ingredients"]):
           payment = process_coins()
           if is_transaction_successful(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])
    else:
        print("You have entered an invalid option. Please try again. ")

# ----------------------------------------------------------------------------------------------------------------------
# My own solution:
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# # Exit the program when user typed "off"
# turn_off_machine = False

# # Store money in a variable
# cash_register = 0

# while not turn_off_machine:
#     # Prompt the user to select between choices of coffee
#     user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

#     # Exit the loop when user typed "off"
#     if user_input == "off":
#         print("Coffee machine will be turned off now.")
#         turn_off_machine = True

#     # When the user types "espresso"
#     elif user_input == "espresso":
#         if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
#             if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
#                 resources["water"] -= MENU["espresso"]["ingredients"]["water"]
#                 resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
#                 print("Please pay: $", MENU["espresso"]["cost"])
#                 cash_register += MENU["espresso"]["cost"]
#                 print("Here is your espresso. Enjoy!")
#             else:
#                 print("Sorry there is not enough coffee.")
#         else:
#             print("Sorry there is not enough water.")
    
#     # When the user types "latte"
#     elif user_input == "latte":
#         if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
#             if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
#                 if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
#                     resources["water"] -= MENU["latte"]["ingredients"]["water"]
#                     resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
#                     resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
#                     print("Please pay: $", MENU["latte"]["cost"])
#                     cash_register += MENU["latte"]["cost"]
#                     print("Here is your latte. Enjoy!")
#                 else:
#                     print("Sorry there is not enough coffee.")
#             else:
#                 print("Sorry there is not enough milk.")
#         else:
#             print("Sorry there is not enough water.")
    
#     # When the user types "cappuccino"
#     elif user_input == "cappuccino":
#         if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
#             if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
#                 if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
#                     resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
#                     resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
#                     resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
#                     print("Please pay: $", MENU["cappuccino"]["cost"])
#                     cash_register += MENU["cappuccino"]["cost"]
#                     print("Here is your cappuccino. Enjoy!")
#                 else:
#                     print("Sorry there is not enough coffee.")
#             else:
#                 print("Sorry there is not enough milk.")
#         else:
#             print("Sorry there is not enough water.")
    
#     # When the user types "report"
#     elif user_input == "report":
#         print(f"Water: {resources['water']} ml")
#         print(f"Milk: {resources['milk']} ml")
#         print(f"Coffee: {resources['coffee']} g")
#         print(f"Money: $ {cash_register}")