# Advanced Python Arguments

# def add(n1, n2):
#     return n1 + n2

# Unlimited Positional Arguments *args - define a function and specify an unlimited/unspecified number of inputs
# The '*' sign tells python that the function can accept any number of arguments
# args is just the default name but we can change it e.g. *numbers
def add(*args):
    # args is a type tuple so the output will be in a ()
    print(type(args))
    print(args[0])
    sum = 0
    # loop through a tuple
    for n in args:
        sum += n
    return sum

print(add(1, 2))

# Many keyworded arguments **kwargs - define a function and specify an unlimited/unspecified number of keyword arguments
# The "**" sign tells python that the function can accept any number of keyword arguments
def calculate(n, **kwargs):
    # kwargs is a type dictionary so the output will be in a {'key':value}
    print(type(kwargs))
    
    # loop through a dict
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# "add" becomes a key, "3" becomes the value
# "multiply" becomes a key, "5" becomes the value
calculate(2, add=3, multiply=5)

# example with Class
class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        
        # using get will return None instead of keyError
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")

my_car = Car(make="VW", model="GTI", color="white")
print(my_car.make)
print(my_car.model)
print(my_car.color)