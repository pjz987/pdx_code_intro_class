# letter_to_number.py
import string
user_letter = input("Give me a letter: ").lower()
number = string.ascii_lowercase.index(user_letter) + 1
print(f"{user_letter.upper()} is the {number}th letter of the alphabet.")

# number_to_letter.py

import string
user_number = int(input("Give me a number: "))
letter = string.ascii_uppercase[user_number -1]
print(f"{letter} is the {user_number}th letter of the alphabet.")
