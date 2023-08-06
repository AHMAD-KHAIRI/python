# minimal flask application
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye") # assigning a decorator function
def say_bye():
    return "Bye"

# To run flask, type in the console: python -m flask --app hello run

# kernel: refers to the actual program that interfaces with the hardware, Core of the OS
# shell: refers to the user interface, for human to interact with the kernel
# 2 variants to shell: 1) GUI, 2) CLI - Command Line Interface

# Instead of typing the command in the console, we can just include the code below and run normally:
if __name__ == "__main__":
    app.run()

