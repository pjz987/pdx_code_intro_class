# lab13encode_rot.py

'''
Write a program that prompts the user for a character, and encodes it with ROT13.  Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Hint: Keep numbers in the 0 through 25 range using %.
'''
import string
user_letter = input("Give me a letter: ").lower()
number = string.ascii_lowercase.index(user_letter) + 1

rot13_num = (number + 13) % 26

rot13_let = string.ascii_uppercase[rot13_num - 1]

print(f"ROT13 for {user_letter.upper()} is {rot13_let}.")

'''
Advanced Version 1
Let the user type a string, and encode that string. For each character, find the corresponding character, add it to an output string.
'''

# user_string = list(input("Give me a string: ").lower())
# counter = 0
# while True:
#     str_index =
