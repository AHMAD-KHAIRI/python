# minimal flask application
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    # render html with inline css
    return "<h1 style='text-align: center'>Hello, World!</h1> \
    <p>This is a paragraph.</p> \
    <img src='https://media.giphy.com/media/sFTWiBKYYWKVa/giphy.gif'>"
    # return "<p>Hello, World!</p>"

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/bye") # assigning a decorator function
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>") # creating variable paths and converting path to a specified data type
# @app.route("/username/<name>")
def greet(name, number):
    return f"Hello {name}! You are {number} years old!"


# To run flask, type in the console: python -m flask --app hello run

# kernel: refers to the actual program that interfaces with the hardware, Core of the OS
# shell: refers to the user interface, for human to interact with the kernel
# 2 variants to shell: 1) GUI, 2) CLI - Command Line Interface

# Instead of typing the command in the console, we can just include the code below and run normally:
if __name__ == "__main__":
    # app.run()
    app.run(debug=True) # run the flask app in debug mode to auto-reload

