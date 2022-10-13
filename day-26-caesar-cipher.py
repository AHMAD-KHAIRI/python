# 85. Caesar Cipher Part 1
# Coded on 10.08.2022

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

num_of_char_in_alphabet = len(alphabet)

num_of_char_in_text = len(text)

text_to_list = list(text)

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        # find the letter using index() method. The index() method finds the first occurrence of the specified value
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

# 86. Caesar Cipher Part 2 - Decryption

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    decipher_text = ""
    for letter in cipher_text:
        # find the letter using index() method. The index() method finds the first occurrence of the specified value
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decipher_text += new_letter
    print(f"The decoded text is {decipher_text}")
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)

# How to compare between two strings and find the position
# test_string = "abcdefghijklmnopqrstuvwxyz"
# msg = input("Type something: ").lower()

# def find_alphabet_in(message):
#     for letter in message:
#         position = test_string.index(letter)
#         print(position)

# find_alphabet_in(message=msg)

