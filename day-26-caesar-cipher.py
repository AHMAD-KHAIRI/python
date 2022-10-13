# 85. Caesar Cipher Part 1
# Coded on 10.08.2022

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        # decode: 5 * -1 = -5
        # encode: 12 + (-5) = 7
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         # find the letter using index() method. The index() method finds the first occurrence of the specified value
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     decipher_text = ""
#     for letter in cipher_text:
#         # find the letter using index() method. The index() method finds the first occurrence of the specified value
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decipher_text += new_letter
#     print(f"The decoded text is {decipher_text}")

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)

# How to compare between two strings and find the position
# test_string = "abcdefghijklmnopqrstuvwxyz"
# msg = input("Type something: ").lower()

# def find_alphabet_in(message):
#     for letter in message:
#         position = test_string.index(letter)
#         print(position)

# find_alphabet_in(message=msg)

