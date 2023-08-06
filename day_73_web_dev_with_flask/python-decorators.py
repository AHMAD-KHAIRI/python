# Recap from functions:
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(multiply, 2, 3)
print(result)

# Nested functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

# nested_function() # calling a nested function will generate a NameError where the function is not defined
outer_function() # output: I'm outer\nI'm inner

def outer_function_1():
    print("I'm outer")

    def nested_function_1():
        print("I'm inner")

    return nested_function_1

# Return a function from another function
inner_function = outer_function_1() # output: I'm outer
inner_function() # output: I'm inner


# Python decorators: Decorators functions as a function that is going to give additional functionality
import time

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function

@delay_decorator # known as syntactic sugar
def say_hello():
    # time.sleep(2)
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello() # This funtion will have a delay because a decorator has been assisgned ("@" sign)
say_bye() # This funtion will have a delay because a decorator has been assisgned ("@" sign)
say_greeting() # This function will not have a delay because we do not assign the decorator

# we can also do it this way:
decorated_function = delay_decorator(say_greeting)
decorated_function()