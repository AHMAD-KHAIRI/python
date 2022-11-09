# 103. Calculator

from day30calculatorart import logo

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

# recursion
def calculator():
    print(logo)
    # Asks user to input the first number
    num1 = float(input("What's the first number?: "))

    # Loop through dictionary and print the symbols (keys) and asks the user to choose
    for symbol in operations:
        print(symbol)

    # create a while loop
    should_continue = True
    while should_continue:

        # Asks user to input the symbol
        operation_symbol = input("Pick an operation: ")

        # Asks user to input the second number
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Asks the user if they should continue or not
        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
