# handling IndexError in a list

fruits = ["Apple", "Orange", "Pear"]

# before exception handling
# def pie(index):
    # fruit = fruits[index]
    # print(f"{fruit} pie")

# after catching exceptions
def pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(f"{fruit} pie")

pie(4)