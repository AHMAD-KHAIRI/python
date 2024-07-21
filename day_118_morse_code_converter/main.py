# Assignment 1: Text to Morse Code Converter
# You will use what you've learnt to create a text-based (command line) 
# program that takes any String input and converts it into Morse Code.

# # Solution:
# print("Welcome to the Text to Morse Code Converter!")

# # create a dictionary of Morse Code characters
# morse_code_chars = {
#     "a": ".-",
#     "b": "-...",
#     "c": "-.-.",
#     "d": "-..",
#     "e": ".",
#     "f": "..-.",
#     "g": "--.",
#     "h": "....",
#     "i": "..",
#     "j": ".---",
#     "k": "-.-",
#     "l": ".-..",
#     "m": "--",
#     "n": "-.",
#     "o": "---",
#     "p": ".--.",
#     "q": "--.-",
#     "r": ".-.",
#     "s": "...",
#     "t": "-",
#     "u": "..-",
#     "v": "...-",
#     "w": ".--",
#     "x": "-..-",
#     "y": "-.--",
#     "z": "--..",
#     "0": "-----",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----."
# }

# # save the input text in a variable
# string_text = str(input("Enter Your Text to Convert to Morse Code:").lower())

# # create an empty list to store the results of the conversion
# morse_code_text = []

# # separate and compare each letter in the string_text with the morse code
# for letter in string_text:
#     if letter == "a":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "b":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "c":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "d":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "e":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "f":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "g":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "h":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "i":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "j":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "k":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "l":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "m":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "n":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "o":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "p":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "q":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "r":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "s":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "t":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "u":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "v":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "w":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "x":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "y":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "z":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "0":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "1":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "2":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "3":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "4":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "5":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "6":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "7":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "8":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == "9":
#         morse_code_text.append(morse_code_chars[letter])
#     elif letter == " ":
#         morse_code_text.append(" ")
#     else:
#         morse_code_text.append("")

# print(f"Your Text: {string_text}, converted into Morse Code is: {morse_code_text}.")


# Further improvement to solution:

morse_code_chars = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

morse_code_text = []

def text_to_morse(string_text):
    for char in string_text:
        # if the letters match in the morse code dict
        if char in morse_code_chars:
            morse_code_text.append(morse_code_chars[char])
        # if there are spaces in the text
        elif char == " ":
            morse_code_text.append(" ")
        # for unknown chars, put a ?
        else:
            morse_code_text.append("?")

print("Welcome to the Text to Morse Code Converter!")
print("""
 __ __    __    ___    __   ___      ___   __    __    ___  
|  V  |  /__\  | _ \ /' _/ | __|    / _/  /__\  | _\  | __| 
| \_/ | | \/ | | v / `._`. | _|    | \__ | \/ | | v | | _|  
|_| |_|  \__/  |_|_\ |___/ |___|    \__/  \__/  |__/  |___| 
  ___   __    __  _   _   _   ___   ___   _____   ___   ___  
 / _/  /__\  |  \| | | \ / | | __| | _ \ |_   _| | __| | _ \ 
| \__ | \/ | | | ' | `\ V /' | _|  | v /   | |   | _|  | v / 
 \__/  \__/  |_|\__|   \_/   |___| |_|_\   |_|   |___| |_|_\ 
      """)
string_text = str(input("Enter Your Text to Convert to Morse Code:").lower())
text_to_morse(string_text)
print(f"Your Text: {string_text}, converted into Morse Code is: {morse_code_text}.")