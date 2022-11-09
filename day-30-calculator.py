# 103. Calculator

from day30calculatorart import logo
print(logo)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# create a dictionary names operations
# use symbols (+, -, *, /) as keys
# values are the names of the functions

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Asks user to input the first number
num1 = int(input("What's the first number?: "))

# Loop through dictionary and print the symbols (keys) and asks the user to choose
for symbol in operations:
    print(symbol)

# Asks user to input the symbol
operation_symbol = input("Pick an operation: ")

# Asks user to input the second number
num2 = int(input("What's the next number?: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
